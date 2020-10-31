import os
import shutil
import time

def main():

	gt30files = 0
	gt30folders = 0

	path = "/Users/sudha/Desktop/C99Pro/test"

	days = 30

	seconds = time.time() - (days * 24 * 60 * 60)

	if os.path.exists(path):
		for root_folder, folders, files in os.walk(path):
			if seconds >= getfileorfolderage(root_folder):
				remove_folder(root_folder)
				gt30folders += 1

				break

			else:

				for folder in folders:

					folder_path = os.path.join(root_folder, folder)
					if seconds >= getfileorfolderage(folder_path):
						remove_folder(folder_path)
						gt30folders += 1

				for file in files:
					file_path = os.path.join(root_folder, file)
					if seconds >= getfileorfolderage(file_path):
						remove_file(file_path)
						gt30files += 1

		else:
			if seconds >= getfileorfolderage(path):
				remove_file(path)
				gt30files += 1

	else:
		print(f'"{path}" is not found')
		gt30files += 1

	print(f"Total folders deleted: {gt30folders}")
	print(f"Total files deleted: {gt30files}")


def remove_folder(path):
	if not shutil.rmtree(path):
		print(f"{path} is removed successfully")

	else:
		print(f"Unable to delete the "+path)



def remove_file(path):
	if not os.remove(path):
		print(f"{path} is removed successfully")

	else:
		print("Unable to delete the "+path)


def getfileorfolderage(path):
	ctime = os.stat(path).st_ctime
	return ctime


if __name__ == '__main__':
	main()
