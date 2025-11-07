import argparse
import logging
import sys
import numpy as np
import pandas as pd

#!/usr/bin/env python3
"""
task-3.py
Healthcare patient records cleaning script.

Usage:
    python task-3.py --input patient_records.csv --output patient_records_cleaned.csv
"""




def setup_logging():
        logging.basicConfig(
                level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s"
        )


def coerce_common_numeric(df, names):
        for name in names:
                if name in df.columns:
                        df[name] = pd.to_numeric(df[name], errors="coerce")
        return df


def fill_numeric_means(df):
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        for col in numeric_cols:
                mean_val = df[col].mean(skipna=True)
                if np.isnan(mean_val):
                        continue
                df[col].fillna(mean_val, inplace=True)
                logging.info("Filled numeric column '%s' missing values with mean=%.4f", col, mean_val)
        return df


def convert_height_to_meters(df):
        # If there's an explicit height_cm column -> convert and create/replace height_m
        if "height_cm" in df.columns:
                df["height_m"] = pd.to_numeric(df["height_cm"], errors="coerce") / 100.0
                df.drop(columns=["height_cm"], inplace=True)
                logging.info("Converted 'height_cm' -> 'height_m' (meters)")
                return df

        # If there's a 'height' column, detect units by typical range and convert if needed
        if "height" in df.columns:
                col = pd.to_numeric(df["height"], errors="coerce")
                median = col.median(skipna=True)
                if pd.notna(median) and median > 3:  # likely in centimeters (e.g., 170)
                        df["height_m"] = col / 100.0
                        df.drop(columns=["height"], inplace=True)
                        logging.info("Detected 'height' in cm (median=%.2f) and converted to 'height_m' (meters)", median)
                else:
                        # assume already in meters
                        df["height_m"] = col
                        df.drop(columns=["height"], inplace=True)
                        logging.info("Kept 'height' as meters into 'height_m' (median=%.2f)", median)
        return df


def clean_categorical(df):
        # Normalize common gender/sex labels
        gender_cols = [c for c in df.columns if c.lower() in ("gender", "sex")]
        gender_map = {
                "m": "Male",
                "male": "Male",
                "f": "Female",
                "female": "Female",
                "woman": "Female",
                "man": "Male",
                "other": "Other",
                "non-binary": "Other",
                "nonbinary": "Other",
                "nb": "Other",
        }
        for col in gender_cols:
                s = df[col].astype(str).str.strip().str.lower()
                mapped = s.map(gender_map).fillna(s.str.capitalize())
                mapped.replace({"nan": np.nan}, inplace=True)
                df[col] = mapped
                logging.info("Standardized gender labels in column '%s'", col)

        # For other object columns, do sensible cleanup: strip and title-case
        obj_cols = df.select_dtypes(include=["object"]).columns.tolist()
        for col in obj_cols:
                if col in gender_cols:
                        continue
                df[col] = df[col].where(df[col].notna(), None)
                try:
                        df[col] = df[col].astype(str).str.strip()
                        # Avoid turning numeric-like strings into titles (e.g., codes); only title-case short words
                        df[col] = df[col].apply(lambda v: v.title() if isinstance(v, str) and v.isalpha() else v)
                except Exception:
                        pass
        return df


def drop_irrelevant_columns(df):
        candidates = {"patient_id", "id", "record_id", "ssn"}
        to_drop = [c for c in df.columns if c.lower() in candidates]
        if to_drop:
                df.drop(columns=to_drop, inplace=True)
                logging.info("Dropped irrelevant columns: %s", to_drop)
        return df


def main(args):
        setup_logging()
        logging.info("Loading data from %s", args.input)
        try:
                df = pd.read_csv(args.input)
        except Exception as e:
                logging.error("Failed to read input CSV: %s", e)
                sys.exit(1)

        # Normalize empty strings to NaN
        df.replace(r"^\s*$", np.nan, regex=True, inplace=True)

        # Try coercing commonly numeric-named columns which may be strings
        common_numeric_names = [
                "blood_pressure",
                "systolic_bp",
                "diastolic_bp",
                "heart_rate",
                "pulse",
                "age",
                "weight",
                "height",
                "height_cm",
                "bmi",
        ]
        df = coerce_common_numeric(df, common_numeric_names)

        # Fill missing numeric values with column mean
        df = fill_numeric_means(df)

        # Convert heights from cm to meters
        df = convert_height_to_meters(df)

        # Standardize categorical labels
        df = clean_categorical(df)

        # Drop irrelevant identifiers
        df = drop_irrelevant_columns(df)

        # Final: drop columns that are completely empty
        empty_cols = [c for c in df.columns if df[c].isna().all()]
        if empty_cols:
                df.drop(columns=empty_cols, inplace=True)
                logging.info("Dropped empty columns: %s", empty_cols)

        # Save cleaned file
        try:
                df.to_csv(args.output, index=False)
                logging.info("Saved cleaned dataset to %s", args.output)
        except Exception as e:
                logging.error("Failed to write output CSV: %s", e)
                sys.exit(1)


if __name__ == "__main__":
        p = argparse.ArgumentParser(description="Clean healthcare patient records CSV")
        p.add_argument("--input", "-i", default="patient_records.csv", help="Input CSV path")
        p.add_argument(
                "--output", "-o", default="patient_records_cleaned.csv", help="Output CSV path"
        )
        args = p.parse_args()
        main(args)