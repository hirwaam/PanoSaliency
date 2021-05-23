import pickle
import csv
path_csv = './data/foin7.csv'

if __name__ == "__main__":
    #TODO: a simple example to load a saliency dataset file
    #RETURN: the values of the first record of the file. The record includes: timestamp, fixation_list, and saliency_map
    #note: this script assumes the dataset has been download from the LINK provided in the ./data folder
    
    #load the dataset file named `saliency_ds1_topicparis` (ds=1, video=paris). Assuming the dataset file is in ./data folder
    data = pickle.load(open('./data/saliency_ds2_topic0','rb'))
    
    with open(path_csv,'w') as f:
        writer = csv.writer(f)
        for line in data: writer.writerow(line)
        
    #pickle_out = open("./data/dict.pickle","wb")
    #pickle.dump(data, pickle_out)
    #pickle_out.close()
    
    #access the first record
    #timestamp, fixation_list, saliency_map = data[5]
    
    #print out the values of fields in the first record
    #print (timestamp)
    #print (fixation_list)
    #print (saliency_map)
    #print (data)