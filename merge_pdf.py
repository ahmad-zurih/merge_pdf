import argparse, sys, random
from PyPDF2 import PdfFileMerger, PdfFileReader

def create_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='program that merge pdf files into one file')
    parser.add_argument('input_files',
                        help='pdf input files',
                        type=argparse.FileType("rb"),
                        nargs='+',
                        default=[sys.stdin])
    parser.add_argument("--file_name", "--f",
                        help="allows the user to insert the output file name",
                        type=str)
    return parser


def merge_pdf(pdf_files, out_file=f"output{random.randint(10000,99999)}.pdf"):
    """
    function that takes multples pdf files and merge them into one pdf file in order
    """
    merger = PdfFileMerger()
    for file in pdf_files:
        pdf_file = PdfFileReader(file, strict=False)
        merger.append(pdf_file)
    with open(out_file, "wb") as out:
        merger.write(out)
    merge_pdf.argu = locals()
    return None

def main():
    parser = create_argument_parser()
    args = parser.parse_args()
    if args.file_name:
        merge_pdf(args.input_files, args.file_name)
        print(f"Your file is saved into your directory as {args.file_name}")
    else:
        merge_pdf(args.input_files)
        print(f"Your file is saved into your directory as {merge_pdf.argu['out_file']}")

if __name__ == '__main__':
    main()
