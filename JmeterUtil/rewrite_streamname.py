# rewrite stream name
import csv


def rewrite_streamname(fname, stream_name):
    csv_data=[]
    with open(fname, "r") as reader:
        ex_read = csv.reader(reader)
        csv_data = list(ex_read)
        csv_data[1][0] = stream_name
        print((csv_data))

    with open(fname, "w", newline="")as writer:
        output_writer = csv.writer(writer)
        for csv_element in csv_data:
            print(csv_element)
            output_writer.writerow(csv_element)


if __name__ == "__main__":
    rewrite_streamname("image/test.csv", "saahajimeyou")
