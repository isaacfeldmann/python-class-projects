from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://www.course-catalog.com/mercyhurst/C/2024-2025/degrees-by-department'

web_page = urlopen(url).read().decode('UTF-8')

#  creating soup object
soup = BeautifulSoup(web_page, 'html.parser')

table_tags_list = soup.find_all('table', attrs={'class':'normal-table'})

for table_tag in table_tags_list:
    print(table_tag['summary'])


dept_name = input('enter department name: ')

for table_tag in table_tags_list:
    if table_tag['summary'].lower() == dept_name:
        print(f'programs in {dept_name}: ')

        tbody_tag = table_tag.find('tbody')
        tr_tag_list = tbody_tag.find_all('tr')

        for tr_tag in tr_tag_list:
            td_tag_list = tr_tag.find_all('td')
            program_name_td_tag = td_tag_list[0]
            print(program_name_td_tag.text.strip())
        program_name = input('choose a program name: ')

        for tr_tag in tr_tag_list:
            td_tag = tr_tag.find('td')

            if td_tag.text.strip().lower() == program_name:
                a_tag = td_tag.find('a')
                print(a_tag['href'])
                program_url = a_tag['href']
                break

        program_page = urlopen(program_url).read().decode('UTF-8')
        program_soup = BeautifulSoup(program_page, 'html.parser')
        course_row_div_tag_list = program_soup.find_all('div', attrs={'class':'crt-m'})

        for course_row_div_tag in course_row_div_tag_list:
            courseID_div_tag = course_row_div_tag.find('div', attrs={'class':'crt-2'})
            courseName_div_tag = course_row_div_tag.find('div', attrs={'class':'crt-3'})

            if courseID_div_tag and courseName_div_tag:
                print(courseID_div_tag.text.strip(), '\t', courseName_div_tag.text.strip())

