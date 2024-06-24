def main():

	with open("books/frankenstein.txt") as f:
		file_contents = f.read()
	print(file_contents)

	words = file_contents.split()
	word_count = len(words)
	print(word_count)

	text = file_contents.lower()
	counts = {}
	for character in text:
		if character.isalpha():
			if character in counts:
				counts[character] += 1
			else:
				counts[character] = 1

	print(counts)

	counts_list = [{"character": char, "num": num} for char, num in counts.items()]

	def sort_on(item):
		return item["num"]

	counts_list.sort(reverse=True, key=sort_on)

	print("--- Begin report of books/frankenstein.txt ---")
	for item in counts_list:
		print(f"The '{item['character']}' character was found {item['num']} times")
	print("--- End report ---")

if __name__ == "__main__":
	main()
