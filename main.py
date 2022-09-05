import csv, re


if __name__ == '__main__':
    with open("phonebook_raw.csv", encoding='utf-8') as f:
      rows = csv.reader(f, delimiter=",")
      contacts_list = list(rows)

    new_list = [contacts_list.pop(0)]
    names = {}
    i = 1
    for row in contacts_list:
        phone = re.sub("^8", "+7", row[5])
        phone = re.sub("[\s()-]", "", phone)
        if len(phone) > 0:
            phone = phone[:2] + "(" + phone[2:5] + ")" + phone[5:8] + "-" + phone[8:10] + "-" + phone[10:]
        row[5] = phone.lower().replace("д", " д")
        # row[5] = re.sub("д", " д", phone.lower())
        fio = row[0] + " " + row[1] + " " + row[2]
        new_row = fio.split(" ")[:3] + row[3:7]
        name = new_row[0] + " " + new_row[1]
        if name not in names.keys():
            names[name] = i
            new_list.append(new_row)
            i += 1
        else:
            for p in range(7):
                if new_list[names[name]][p] != new_row[p]:
                    new_list[names[name]][p] += new_row[p]

    with open("phonebook.csv", "w", encoding='utf-8') as f:
      datawriter = csv.writer(f, delimiter=',')
      datawriter.writerows(new_list)  # почему-то лишние пустые строки записывет в файл
