'''
excel 파일을 읽어 텍스트 파일 저장
1. 메이저리그 야구 구장 목록 엑셀파일에서 구장의 위치가 미국이 아닌 다른 국가에 있는 목록을 조회
2. 해당 데이터를 park_outside_us.txt 파일로 저장
'''
import openpyxl

def find_parks_not_in_us():
	# 엑셀파일(워크북) 열기
	wb = openpyxl.load_workbook('example.xlsx')

	# 워크시트 열기
	sheet = wb.get_sheet_by_name('Sheet1')

	# 결과를 저장할 리스트
	parklist = []

	# 파일을 로우 단위로 읽어 국가가 US가 아닌 로우를 파일로 쓴다
	# 1. 파일을 읽을 범위를 결정
	# 2. 로우를 순회하면서 US가 아닌 로우를 리스트로 만든다.
	for row in sheet[2:sheet.max_row]:
		print(row)
		if row[5].value != 'US':
			parklist.append(row)

	wb.close()  # don't forget!
	return parklist


def make_file(parklist):
	with open('parklist.txt', 'w', encoding='utf-8') as file:
		for item in parklist:
			park_str = make_parkstr(item)
			file.write(park_str + '\n')

def make_parkstr(t):
	result_str = ''
	for item in t:
		result_str += str(item.value) + '\t'

	return result_str

def main():
	parklist = find_parks_not_in_us()
	make_file(parklist)
	print('parklist.txt 파일이 생성되었습니다.')


if __name__ == '__main__':
	main()
