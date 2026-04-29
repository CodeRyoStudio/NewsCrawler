import argparse

from .crawler import crawl_business_news


def main() -> None:
    parser = argparse.ArgumentParser(description="CNN business news crawler")
    parser.add_argument(
        "--output-dir",
        default="output",
        help="Directory for generated txt files (default: output)",
    )
    args = parser.parse_args()

    total = crawl_business_news(output_dir=args.output_dir)
    print(f"Done. Saved {total} articles into {args.output_dir}/")


if __name__ == "__main__":
    main()
