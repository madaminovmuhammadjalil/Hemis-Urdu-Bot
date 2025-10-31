
class excel():
    def exceldj1(self,lessonlist):
        import xlsxwriter
        print(lessonlist)

        new_list = [['first', 'second'], ['third', 'four'], [1, 2, 3, 4, 5, 6],lessonlist]

        with xlsxwriter.Workbook('test.xlsx') as workbook:
            worksheet = workbook.add_worksheet()

            for row_num, data in enumerate(lessonlist):
                worksheet.write_row(row_num, 0, data) \

        return workbook
    # def exceldj(self,lessonlist2):
    #     import xlsxwriter
    #     letter=['A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z']
    #     number=0
    #     son=0
    #     workbook = xlsxwriter.Workbook('hello.xlsx')
    #     worksheet = workbook.add_worksheet()
    #
    #     for i in lessonlist2:
    #         son+=1
    #         #
    #         # worksheet.write('D3', 'Hello world')
    #         worksheet.write(f"{letter[number]}{son}",f"{i}")
    #         number += 1
    #
    #     workbook.close()
    #
    #     return workbook
