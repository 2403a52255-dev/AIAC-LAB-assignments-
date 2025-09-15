import unittest
import re

def bump_version(name):
    # Handle known double extensions (.tar.gz, .tar.bz2, .tar.xz, etc.)
    double_exts = [".tar.gz", ".tar.bz2", ".tar.xz"]
    ext = ""
    base = name

    for dext in double_exts:
        if name.endswith(dext):
            base = name[: -len(dext)]
            ext = dext
            break
    else:
        # Otherwise, split at last dot
        if "." in name:
            base, single_ext = name.rsplit(".", 1)
            ext = "." + single_ext
        else:
            base, ext = name, ""

    # Look for version suffix in base
    match = re.search(r"(.*)_v(\d+)$", base)
    if match:
        prefix, version = match.groups()
        new_version = int(version) + 1
        width = max(len(version), 2)  # preserve padding (min 2)
        return f"{prefix}_v{new_version:0{width}d}{ext}"
    else:
        return f"{base}_v01{ext}"


# ---------- Unit Tests ----------
class TestBumpVersion(unittest.TestCase):
    def test_add_version(self):
        self.assertEqual(bump_version("summary.csv"), "summary_v01.csv")
        self.assertEqual(bump_version("data.txt"), "data_v01.txt")
        self.assertEqual(bump_version("file"), "file_v01")
    
    def test_increment_version(self):
        self.assertEqual(bump_version("report_v1.csv"), "report_v02.csv")
        self.assertEqual(bump_version("log_v09.txt"), "log_v10.txt")
        self.assertEqual(bump_version("notes_v99.md"), "notes_v100.md")
    
    def test_edge_cases(self):
        self.assertEqual(bump_version("archive_v01.tar.gz"), "archive_v02.tar.gz")
        self.assertEqual(bump_version("archive_v9.tar.bz2"), "archive_v10.tar.bz2")
        self.assertEqual(bump_version("my.file_v2.csv"), "my.file_v03.csv")
        self.assertEqual(bump_version("noext_v1"), "noext_v02")
        self.assertEqual(bump_version("justfile"), "justfile_v01")
        self.assertEqual(bump_version("complex.name_v09.backup"), "complex.name_v10.backup")
        self.assertEqual(bump_version("multi.part.name.csv"), "multi.part.name_v01.csv")
        self.assertEqual(bump_version("multi.part.name_v01.csv"), "multi.part.name_v02.csv")
        self.assertEqual(bump_version("bigfile_v0009.csv"), "bigfile_v0010.csv")


# ---------- Demo Run ----------
if __name__ == "__main__":
    files = [
        "my.file_v2.csv",
        "archive_v01.tar.gz",
        "archive_v9.tar.bz2",
        "report_v1.csv",
        "summary.csv",
        "file"
    ]
    print("Sample Input → Output")
    for f in files:
        print(f" {f:30} → {bump_version(f)}")

    print("\nRunning unit tests...\n")
    unittest.main(exit=False)