import os

def get_common_fields():
    fields = {
        "author": input("Enter the author(s): "),
        "title": input("Enter the title: "),
        "year": input("Enter the year: "),
    }
    return fields

def get_article_fields():
    fields = get_common_fields()
    fields["journal"] = input("Enter the journal name: ")
    fields["volume"] = input("Enter the volume: ")
    fields["number"] = input("Enter the issue number: ")
    fields["pages"] = input("Enter the pages (e.g., 12-34): ")
    fields["doi"] = input("Enter the DOI (optional): ")
    return fields

def get_book_fields():
    fields = get_common_fields()
    fields["publisher"] = input("Enter the publisher: ")
    fields["address"] = input("Enter the publisher's address: ")
    fields["edition"] = input("Enter the edition: ")
    fields["isbn"] = input("Enter the ISBN (optional): ")
    return fields

def get_inproceedings_fields():
    fields = get_common_fields()
    fields["booktitle"] = input("Enter the title of the conference proceedings: ")
    fields["organization"] = input("Enter the organization: ")
    fields["pages"] = input("Enter the pages (e.g., 56-78): ")
    fields["doi"] = input("Enter the DOI (optional): ")
    return fields

def get_manual_fields():
    fields = get_common_fields()
    fields["organization"] = input("Enter the organization: ")
    fields["address"] = input("Enter the address: ")
    return fields

def get_thesis_fields(thesis_type):
    fields = get_common_fields()
    fields["school"] = input("Enter the school or institution: ")
    fields["address"] = input("Enter the address: ")
    fields["type"] = thesis_type.capitalize()  # Either "Master's thesis" or "PhD thesis"
    return fields

def get_inbook_fields():
    fields = get_common_fields()
    fields["chapter"] = input("Enter the chapter: ")
    fields["publisher"] = input("Enter the publisher: ")
    fields["address"] = input("Enter the address: ")
    fields["pages"] = input("Enter the pages (e.g., 34-56): ")
    return fields

def get_booklet_fields():
    fields = get_common_fields()
    fields["howpublished"] = input("Enter how it was published: ")
    fields["address"] = input("Enter the address: ")
    return fields

def get_incollection_fields():
    fields = get_common_fields()
    fields["booktitle"] = input("Enter the title of the book: ")
    fields["publisher"] = input("Enter the publisher: ")
    fields["pages"] = input("Enter the pages (e.g., 123-145): ")
    fields["address"] = input("Enter the address: ")
    return fields

def get_proceedings_fields():
    fields = get_common_fields()
    fields["editor"] = input("Enter the editor: ")
    fields["organization"] = input("Enter the organization: ")
    fields["publisher"] = input("Enter the publisher: ")
    fields["address"] = input("Enter the address: ")
    fields["volume"] = input("Enter the volume: ")
    fields["series"] = input("Enter the series: ")
    fields["pages"] = input("Enter the pages (e.g., 1-10): ")
    return fields

def get_techreport_fields():
    fields = get_common_fields()
    fields["institution"] = input("Enter the institution: ")
    fields["number"] = input("Enter the report number: ")
    return fields

def get_unpublished_fields():
    fields = get_common_fields()
    fields["note"] = input("Enter a note: ")
    return fields

def write_entry_to_file(entry_type, fields):
    with open("papers.bib", "a") as file:
        file.write(f"\n@{entry_type}{{\n")
        for key, value in fields.items():
            if value:  # Only write fields that have a value
                file.write(f"  {key} = {{{value}}},\n")
        file.write("}\n")

def main():
    entry_type = input("Enter the type of entry (article, book, inproceedings, manual, mastersthesis, phdthesis, inbook, booklet, incollection, proceedings, techreport, unpublished): ").strip().lower()

    if entry_type == "article":
        fields = get_article_fields()
    elif entry_type == "book":
        fields = get_book_fields()
    elif entry_type == "inproceedings":
        fields = get_inproceedings_fields()
    elif entry_type == "manual":
        fields = get_manual_fields()
    elif entry_type == "mastersthesis" or entry_type == "phdthesis":
        fields = get_thesis_fields(entry_type)
    elif entry_type == "inbook":
        fields = get_inbook_fields()
    elif entry_type == "booklet":
        fields = get_booklet_fields()
    elif entry_type == "incollection":
        fields = get_incollection_fields()
    elif entry_type == "proceedings":
        fields = get_proceedings_fields()
    elif entry_type == "techreport":
        fields = get_techreport_fields()
    elif entry_type == "unpublished":
        fields = get_unpublished_fields()
    else:
        print(f"Entry type '{entry_type}' is not supported.")
        return

    write_entry_to_file(entry_type, fields)
    print(f"The entry has been added to papers.bib.")

if __name__ == "__main__":
    main()