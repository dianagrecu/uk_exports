import os
import subprocess

exports = "export_files.txt"
funcs = "func_names.txt"


def find_defs():
	os.system(f"find ./ -maxdepth 7 -name exportsyms.uk > {exports}")

	with open(funcs, 'w') as res_file:
		with open(exports) as f:
			for export_file_path in f:
				with open(export_file_path.strip()) as file:
					for func_name in file:
						if func_name[0] != '#':
							res_file.write(func_name)

	os.system(f"sed -i '/^$/d' {funcs}")

	with open("test.txt") as file:
		for func_name in file:
			print(f"curr func name is: {func_name.strip()}")
			# print(os.popen(f"grep -R \"\b{func_name.strip()}\b\" * | grep \".h:[a-z]\" >> file.txt").read())


if __name__ == "__main__":
	find_defs()

