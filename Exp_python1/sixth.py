def merge_files(file_a, file_b, file_c):
    with open(file_a, 'r') as fa, open(file_b, 'r') as fb:
        content_a = fa.readlines()
        content_b = fb.readlines()

    merged_content = sorted(content_a + content_b)

    with open(file_c, 'w') as fc:
        fc.writelines(merged_content)

merge_files('a.txt', 'b.txt', 'c.txt')
