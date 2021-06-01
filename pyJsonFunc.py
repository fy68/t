def dump_json(obj,fp_name,encoding:str,indent:int=0,ensure_ascii:bool=True):
    if encoding:
        with open (fp_name,encoding=encoding) as f:
            json.dump(obj,f,indent=indent,ensure_ascii=ensure_ascii)
    else:
        with open (fp_name) as f:
            json.dump(obj,f,indent=indent,ensure_ascii=ensure_ascii)

def load_json(fp_name,encoing:str):
    if encoing:
        with open(fp_name, encoding=encoding) as f:
            return json.load(f)
    else:
        with open(fp_name) as f:
            return json.load(f)
