l1 = [10,20,30,40,50,20]
count = 0
for i in l1:
    if i == 20:  #  > , <  , >=, <= , == != 
        count = count + 1
        print(count)


print("20 is present in l1 for", count, "times")

l2 = [1,2,3,4,5,6,7,8,9,10]
even_number = []
odd_number = []

for i in l2:
    if i % 2 == 0:    # 2/2  if we get reminder 0  else it is odd number 
        even_number.append(i)
    else:
        odd_number.append(i)

print("Even numbers in l2 are:", even_number)
print("Odd numbers in l2 are:", odd_number)


file_name = ["sample.pdf", "report.docx", "presentation.pptx", "data.xlsx", "notes.txt", "DATA.PDF"]
pdf_files = []

for i in file_name:
    if i.endswith(".pdf") or i.endswith(".PDF"):    # "sample.pdf".endswith(".pdf")  # True
        pdf_files.append(i)

print("PDF files in the list are:", pdf_files)


doc_files = []
ppt_files = []

# function endswith , startswith
for i in file_name:
    if i.endswith(".pdf") or i.endswith(".PDF"):    # "sample.pdf".endswith(".pdf")  # True
        pdf_files.append(i)
    elif i.endswith(".docx") or i.endswith(".DOCX"):
        doc_files.append(i)
    elif i.endswith(".pptx") or i.endswith(".PPTX"):
        ppt_files.append(i)


print("PDF files in the list are:", pdf_files)
print("DOCX files in the list are:", doc_files)
print("PPTX files in the list are:", ppt_files)

    
# dynamically get username and password 
# username and password is not null and username == admin 
# you are allow to login else permission denied


file_name = ["sample.pdf", "report.docx", "presentation.pptx", "data.xlsx", "notes.txt", "DATA.PDF"]

for i in file_name:
    if i.endswith(".pdf") or i.endswith(".PDF"):    # "sample.pdf".endswith(".pdf")  # True
        pdf_files.append(i)

pdf_files = [i for i in file_name if i.endswith(".pdf") or i.endswith(".PDF")]  # one liner coding 
print("PDF files in the list with one liner:", pdf_files)

# flow and logic of the program is more important than the code itself.

list_user = ["admin", "root","superuser1"]
if not any of the user in list_user user can do only read the files and view the files
if user in list_user then they can read, write and delte the files ?
    if user in list_user  and admin then they can read, write, delete and create the files
    if user in list_user  and root then they can read, write and delete the files but they cannot create the files

