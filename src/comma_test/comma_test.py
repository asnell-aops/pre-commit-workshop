import sqlparse

def detect_extra_commas(filename: str):
    failure = False
    model_file = open(filename)
    model_contents = model_file.read()
    parsed_contents = sqlparse.parse(model_contents)[0]
    model_file.close()

    for token in parsed_contents.tokens:
        if type(token) is sqlparse.sql.Punctuation and token.value == ',':
            failure = True

    return int(failure)