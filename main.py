import os

ENTRY = "I simulated the deadline 10,000 times and hit it in every one. This timeline was the only one I didn't test."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
