import xlrd  # 导入读模块
import xlwt  # 导入写模块


def main():
    # 打开data.xlsx文件读取数据
    data = xlrd.open_workbook('data.xlsx')

    # 读取第一个（0）表单
    table = data.sheets()[0]

    # 或者通过表单名称获取 table = data.sheet_by_name(u'Sheet1')
    rows = table.nrows
    cols = table.ncols

    # 新建两个list，来存储去重后的数据
    col_one_list = []
    col_three_list = []

    # 创建新的Excel（新的workbook），建议还是用ascii编码
    wb = xlwt.Workbook(encoding='ascii')
    ws = wb.add_sheet('Sheet1')

    # 表头数据先写好
    ws.write(0, 0, label=table.cell(0, 0).value)
    ws.write(0, 1, label=table.cell(0, 1).value)
    ws.write(0, 2, label=table.cell(0, 2).value)

    # 这里是新文档的遍历指针
    k = 1

    # 第一行是表头，略过
    for i in range(1, rows):
        first_value = table.cell(i, 0).value
        second_value = table.cell(i, 1).value
        three_value = table.cell(i, 2).value

        if first_value in col_one_list:
            # 如果第一列的值已经在列表里了，那就比较两个列表中相同位置是否相同
            index = col_one_list.index(first_value)

            if three_value == col_three_list[index]:
                continue
            else:
                col_one_list.append(first_value)
                col_three_list.append(three_value)

                # 不重复的数据写入新文档
                ws.write(k, 0, label=first_value)
                ws.write(k, 1, label=second_value)
                ws.write(k, 2, label=three_value)
        else:
            col_one_list.append(first_value)
            col_three_list.append(three_value)

            # 不重复的数据写入新文档
            ws.write(k, 0, label=first_value)
            ws.write(k, 1, label=second_value)
            ws.write(k, 2, label=three_value)

        k += 1

    # 保存新的文档
    wb.save('new_data.xls')


if __name__ == '__main__':
    main()
