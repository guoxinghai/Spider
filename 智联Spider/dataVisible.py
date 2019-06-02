import xlrd
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.charts import Map
from pyecharts.charts import Page, WordCloud


class DataVisible:
    def __init__(self):
        # 读取excel表
        self.excel = xlrd.open_workbook("data/recruit.xls")
        self.data = self.excel.sheet_by_name("Sheet1")

    def average_salary_bar(self):
        option_list = []
        option_dict = {}
        for i in self.data.col_values(8, 1):
            if i not in option_list:
                option_list.append(i)
            if not option_dict.get(i):
                option_dict[i] = int(0)

        for i in self.data.col_values(8, 1):
            option_dict[i] = option_dict[i] + 1

        option_value_list = list(option_dict.values())
        bar = Bar()
        bar.add_xaxis(option_list)
        print(type(option_value_list))
        bar.add_yaxis("平均薪资", option_value_list)
        bar.set_global_opts(title_opts=opts.TitleOpts(title="平均薪资"))
        bar.render("average_salary.html")

    # 平均薪水玫瑰图
    def average_salary_pie(self):
        option_dict = {}
        for i in self.data.col_values(8, 1):
            if not option_dict.get(i):
                option_dict[i] = int(0)

        for i in self.data.col_values(8, 1):
            option_dict[i] = option_dict[i] + 1

        keys = list(option_dict.keys())
        values = list(option_dict.values())
        key_value = []
        for i in range(0, len(keys)):
            key_value.append((keys[i], values[i]))
        c = (
            Pie()
                .add(
                "",
                key_value,
                radius=["20%", "75%"],
                center=["60%", "65%"],
                rosetype="radius",
                label_opts=opts.LabelOpts(is_show=False),
            )
                .set_global_opts(title_opts=opts.TitleOpts(title="薪资分布玫瑰图"),
                                 legend_opts=opts.LegendOpts(pos_left="30%"))
        )
        c.render("view/平均薪资玫瑰图.html")

    # 城市分布玫瑰图
    def city_pie(self):
        option_dict = {}
        for i in self.data.col_values(10, 1):
            if not option_dict.get(i):
                option_dict[i] = int(0)

        for i in self.data.col_values(10, 1):
            option_dict[i] = option_dict[i] + 1

        keys = list(option_dict.keys())
        values = list(option_dict.values())
        key_value = []
        for i in range(0, len(keys)):
            key_value.append((keys[i], values[i]))
        c = (
            Pie()
                .add(
                "",
                key_value,
                radius=["25%", "75%"],
                center=["60%", "70%"],
                rosetype="radius",
                label_opts=opts.LabelOpts(is_show=False),
            )
                .set_global_opts(title_opts=opts.TitleOpts(title="玫瑰图城市分布"), legend_opts=opts.LegendOpts(pos_left="30%"))
        )
        c.render("view/城市分布玫瑰图.html")

    # 城市分布地图
    def city_map(self):
        option_dict = {}
        for i in self.data.col_values(10, 1):
            if not option_dict.get(i):
                option_dict[i] = int(0)

        for i in self.data.col_values(10, 1):
            option_dict[i] = option_dict[i] + 1

        keys = list(option_dict.keys())
        values = list(option_dict.values())
        key_value = []
        for i in range(0, len(keys)):
            key_value.append((keys[i], values[i]))

        c = (
            Map()
                .add("python程序员", key_value, "china", label_opts=opts.LabelOpts(is_show=True))
                .set_global_opts(
                title_opts=opts.TitleOpts(title="城市分布地图"),
                visualmap_opts=opts.VisualMapOpts(max_=300, is_piecewise=True)
                )
        )
        c.render("view/城市分布地图.html")

    # 学位要求饼图
    def degree_pie(self):
        option_dict = {}
        for i in self.data.col_values(11, 1):
            if not option_dict.get(i):
                option_dict[i] = int(0)

        for i in self.data.col_values(11, 1):
            option_dict[i] = option_dict[i] + 1

        keys = list(option_dict.keys())
        values = list(option_dict.values())
        key_value = []
        for i in range(0, len(keys)):
            key_value.append((keys[i], values[i]))

        c = (
            Pie()
                .add(
                "",
                key_value,
                center=["35%", "50%"],
            )
                .set_global_opts(
                title_opts=opts.TitleOpts(title="学位要求"),
                legend_opts=opts.LegendOpts(pos_left="15%"),
            )
                .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
        )
        c.render("view/学位要求饼图.html")

    # 工作年限饼图
    def year_pie(self):
        option_dict = {}
        for i in self.data.col_values(13, 1):
            if not option_dict.get(i):
                option_dict[i] = int(0)

        for i in self.data.col_values(13, 1):
            option_dict[i] = option_dict[i] + 1

        keys = list(option_dict.keys())
        values = list(option_dict.values())
        key_value = []
        for i in range(0, len(keys)):
            key_value.append((keys[i], values[i]))

        c = (
            Pie()
                .add(
                "",
                key_value,
                center=["35%", "50%"],
            )
                .set_global_opts(
                title_opts=opts.TitleOpts(title="工作年限"),
                legend_opts=opts.LegendOpts(pos_left="15%"),
            )
                .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
        )
        c.render("view/工作年限饼图.html")

    # 额外技能词云
    def year_pie(self):
        option_dict = {}  # 存取关键字
        for i in self.data.col_values(12, 1):
            for j in i.split(','):
                if not option_dict.get(j):
                    option_dict[j] = int(0)

        for i in self.data.col_values(12, 1):
            for j in i.split(','):
                option_dict[j] = option_dict[j] + 1

        key_value = sorted(option_dict.items(), key=lambda x: x[1], reverse=True)
        c = (
            WordCloud()
                .add("", key_value, word_size_range=[1, 100])
                .set_global_opts(title_opts=opts.TitleOpts(title="额外技能词云"))
        )
        c.render("view/额外技能词云图.html")


DataVisible().city_map()
