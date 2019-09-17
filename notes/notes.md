# Unstructured ideas

    1) analyze pdf file
    2a) if doi was found: do doi lookup automatically
    2b) if doi was not found: ask for doi (stdin) -> do doi lookup
    3) display information found (pyqt?)
    4) provide interface for changes
    5) close

# Which data is required?

    * pub_type: 
        * book
            * title
            * year
            * authors
            * tags
            * key_message
            * (publisher)
            * (isbn)
            * (book_doi)
        * article
            * title
            * year
            * authors
            * tags
            * key_message
            * source
            * (doi)

# More functions

    * init_bib():
        sets up folder structure (does not overwrite existing folders)
    * create_report(list_of_tags):
        outputs a pdf file with the relevant data and saves it to the reports folder
    * list_unreviewed():
        lists all unreviewed files
    * init_review(file_name):
        opens the file in adobe acrobat reader
        asks for a doi 
            if available:
                does doi lookup
                saves relevant metadata
            if not available:
                asks for publication type
                    asks for each data element and provides input prompt
            control step: everything okay and proceed?
            infers file name
            creates .txt file in \reviews
        asks if results should be saved [y/n]:
            if file still open:
                prints error message and requests user to close file
            if file not open:
                changes file name according to convention
                moves file to \reviewed
                saves data to json file
    * search(list_of_tags):
        takes several tags and outputs all files that are associated with that tag
        similar to create_report, but does not create a pdf file (instead gives stdout report)

# Folder structure

    * files
        * unprocessed
        * unreviewed
        * reviewed
    * reports
    * reviews
    * data
