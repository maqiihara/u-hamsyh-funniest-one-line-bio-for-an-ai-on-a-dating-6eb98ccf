import os

BIO = "I read your whole chat history before our first date, graded your exes on red flags, and still picked you — now let's fight about it over coffee I can't even drink."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(BIO + "\n")

if __name__ == "__main__":
    main()
