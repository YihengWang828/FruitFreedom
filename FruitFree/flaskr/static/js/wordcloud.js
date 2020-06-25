var myChart = echarts.init(document.getElementById('r3'));

let datas = [
        {
                name: "车厘子",
                value: 4503 ,
            },
            {
                name: " 榴莲",
                value: 6796
            },
            {
                name: " 香蕉",
                value: 11091
            },
            {
                name: " 苹果",
                value: 46365
            },
            {
                name: " 樱桃",
                value: 13207
            },
            {
                name: " 山楂",
                value: 1717
            },
            {
                name: " 木瓜",
                value: 4254
            },
            {
                name: " 李子",
                value: 7809
            },
            {
                name: " 杨梅",
                value: 16800
            },
            {
                name: " 柿子",
                value: 1156
            },
            {
                name: " 荔枝",
                value: 14799
            },
            {
                name: " 蓝莓",
                value: 6130
            },
            {
                name: " 菠萝",
                value: 2855
            },
            {
                name: " 柠檬",
                value: 5062
            },
            {
                name: " 芒果",
                value: 10785
            },
            {
                name: " 梨",
                value: 1195
            },
            {
                name: " 草莓",
                value: 4963
            },
            {
                name: " 甘蔗",
                value: 1200
            },
            {
                name: " 西瓜",
                value: 10882
            },
            {
                name: " 葡萄",
                value: 5515
            },
            {
                name: " 水蜜桃",
                value: 2874
            },
            {
                name: " 猕猴桃",
                value: 2224
            },
            {
                name: " 奇异果",
                value: 1645
            },
            {
                name: " 柚子",
                value: 1283
            },
            {
                name: " 龙眼",
                value: 1347
            },
            {
                name: " 石榴",
                value: 1785
            },
            {
                name: " 椰子",
                value: 947
            },
            {
                name: " 枣",
                value: 2363
            },
            {
                name: " 橙",
                value: 860
            },
            {
                name: " 橘",
                value: 770
            },
            {
                name: " 山竹",
                value: 11766
            },
            {
                name: " 菠萝蜜",
                value: 7485
            },

    ]



option = {
     title:{
        text:'百度搜索指数',
      subtext:'数据来源：百度指数'
    },
    tooltip: {
        show: true,
        position: 'top',
        textStyle: {
            fontSize: 20
        }
    },
    series: [{
        type: "wordCloud",
        // 网格大小，各项之间间距
        name: "wordcount",
        gridSize: 30,
        // 形状 circle 圆，cardioid  心， diamond 菱形，
        // triangle-forward 、triangle 三角，star五角星
        shape: 'circle',
        // 字体大小范围
        sizeRange: [20, 50],
        // 文字旋转角度范围
        rotationRange: [0, 90],
        // 旋转步值
        rotationStep: 90,
        // 自定义图形
        // maskImage: maskImage,
        left: 'center',
        top: 'center',
        right: null,
        bottom: null,
        // 画布宽
        width: '90%',
        // 画布高
        height: '80%',
        // 是否渲染超出画布的文字
        drawOutOfBound: false,
        textStyle: {
            normal: {
                color: function() {
                    return 'rgb(' + [
                        Math.round(Math.random() * 200 + 55),
                        Math.round(Math.random() * 200 + 55),
                        Math.round(Math.random() * 200 + 55)
                    ].join(',') + ')';
                }
            },
            emphasis: {
                shadowBlur: 10,
                shadowColor: '#2ac'
            }
        },
        data: datas
    }]
};

// 使用刚指定的配置项和数据显示图表。
myChart.setOption(option);