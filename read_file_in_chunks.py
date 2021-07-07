def read_file_in_chunks(file, chunk_size):
    while 1:
        chunk_data = file.read(chunk_size)
        print(chunk_data)
        if not chunk_data:
            break

    yield chunk_data


if __name__ == '__main__':
    file = open('english.txt')
    chunk_size = 1024*1024  # 1M

    for chunk in read_file_in_chunks(file, chunk_size):
        print(chunk)

    file.close()