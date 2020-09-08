import ast
import json
import sys
import numpy as np


def analyze_run(datastore, output_path):
    overall = []
    datastore = datastore["traceEvents"]
    for item in datastore:
        if "args" in item:
            name = item["name"]
            item = item["args"]
            if "snapshot" in item:
                item = item["snapshot"]
                if "tensor_description" in item:
                    item = item["tensor_description"]
                    if "allocation_description" in item:
                        item = item.split()
                        store_tensor = [name]
                        sizes = []
                        allo = []
                        for i in range(len(item)):
                            if item[i] == "dtype:":
                                store_tensor.append(item[i+1])
                            if item[i] == "size:":
                                sizes.append(item[i+1])
                            if item[i] == "requested_bytes:":
                                store_tensor.append(str(round(float(item[i+1])/1024**2, 3)))
                            if item[i] == "allocator_name:":
                                allo.append(item[i+1])
                        store_tensor.extend(allo)
                        store_tensor.extend(sizes)
                        while len(store_tensor) < 8:
                            store_tensor.append("null")
                        overall.append(store_tensor)
    overall = np.array(overall)
    sort_by_mems = np.argsort(overall[:,2].astype(np.float))[::-1]
    overall = overall[sort_by_mems]
    np.savetxt(output_path+"/tensor_memory.txt", overall, fmt="%s", delimiter=",")

if __name__ == "__main__":
    print(sys.argv[1])
    with open("timeline.json", 'r') as f:
        datastore = json.load(f)
    analyze_run(datastore, ".")
