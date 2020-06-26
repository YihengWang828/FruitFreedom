var myChart = echarts.init(document.getElementById('echarts6'));

// 指定图表的配置项和数据
option = {
    // title: {
    //     text: '常见水果B族维生素含量(mg/100g)',
    //     subtext: '含量过低的水果约为0',
    //     left: 'center',
    //     textStyle: {
    //         color: '#fff'
    //     },
    //     // top: "5%",
    // },
    tooltip: {
        confine: true,
    },
    xAxis3D: {
        type: 'category',
        name: '水果名称',
        data: ['龙眼', '荔枝', '鲜枣', '菠萝蜜', '香蕉', '杨桃', '桃', '柠檬', '杏', '樱桃', '椰子', '橙', '梨', '猕猴桃', '草莓', '芒果', '苹果', '西瓜'],
        nameGap: 30,
        axisLabel: {
            interval: 0
        },
        nameTextStyle: {
            fontSize: 12
        }
    },
    yAxis3D: {
        type: 'value',
        nameGap: 30,
        name: '核黄素(mg)',
        nameTextStyle: {
            fontSize: 12
        }
    },
    zAxis3D: {
        type: 'value',
        nameGap: 30,
        name: '尼克酸(mg)',
        nameTextStyle: {
            fontSize: 12
        }
    },
    grid3D: {
        boxWidth: 200,
        boxDepth: 80,
        viewControl: {
            // projection: 'orthographic'
        },
        light: {
            main: {
                intensity: 1.2,
                shadow: true
            },
            ambient: {
                intensity: 0.3
            }
        }
    },
    series: [{
        type: 'bar3D',
        data: [
            [0, 0.15, 1.25],
            [1, 0.04, 1.1],
            [2, 0.1, 0.95],
            [3, 0.05, 0.7],
            [4, 0.05, 0.62],
            [5, 0.04, 0.7],
            [6, 0.03, 0.7],
            [7, 0.01, 0.72],
            [8, 0.02, 0.6],
            [9, 0.01, 0.6],
            [10, 0, 0.5],
            [11, 0.03, 0.3],
            [12, 0.03, 0.3],
            [13, 0.01, 0.3],
            [14, 0.05, 0.3],
            [15, 0.06, 0.3],
            [16, 0.01, 0.2],
            [17, 0.01, 0.1],

        ],
        itemStyle: {
            normal: {
                //这里是重点
                color: function (params) {
                    //注意，如果颜色太少的话，后面颜色不会自动循环，最好多定义几个颜色
                    var colorList = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf', '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026', '#d73027', '#f46d43', '#fdae61', '#fee090', '#ffffbf', '#e0f3f8', '#74add1'];
                    return colorList[params.dataIndex]
                }
            }
        },
        shading: 'lambert',

        label: {
            textStyle: {
                fontSize: 16,
                borderWidth: 1
            }
        },

        emphasis: {
            label: {
                textStyle: {
                    fontSize: 20,
                    color: '#900'
                },
                show: false,
            },
            itemStyle: {
                color: '#90ed7d'
            }
        }
    }]
}
// 使用刚指定的配置项和数据显示图表。
myChart.setOption(option);