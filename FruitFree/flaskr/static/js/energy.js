var myChart = echarts.init(document.getElementById('echarts3'));

// 指定图表的配置项和数据
var data = [241, 125, 105, 102, 93, 74, 73, 71, 71, 54, 51, 50, 46, 44, 35, 32, 26,];
var titlename = ['椰子', '鲜枣', '菠萝蜜', '山楂', '香蕉', '柿子', '石榴', '荔枝', '龙眼', '苹果', '桃', '梨', '樱桃', '菠萝', '芒果', '草莓', '西瓜'];
var myColor = ['#1089E7', '#F57474', '#56D0E3', '#1089E7', '#F57474', '#56D0E3', '#F8B448', '#8B78F6', '#F8B448', '#8B78F6'];
option = {
    // backgroundColor: '#fff',
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'shadow',
            shadowStyle: {
                // color: 'rgba(255, 109, 0, 0.8)'
            }
        },
        confine: true,
    },
    // title: {
    //     text: '常见水果所含能量',
    //     // x: 'left',
    //     textStyle: {
    //         fontSize: 20,
    //         color: '#fff'
    //     },
    //     // left: '6%',
    //     top: '5%'
    // },
    //图标位置
    grid: {
        top: '10%',
        left: '23%'

    },
    xAxis: {
        show: false
    },
    yAxis: [{
        show: true,
        data: titlename,
        inverse: true,
        axisLine: {
            show: false
        },
        splitLine: {
            show: false
        },
        axisTick: {
            show: false
        },
        axisLabel: {
            color: '#333',
            formatter: (value, index) => {
                return [
                    `{lg|${index + 1}}  ` + '{title|' + value + '} '
                ].join('\n')
            },
            rich: {
                lg: {
                    backgroundColor: '#8d7fec',
                    color: '#fff',
                    borderRadius: 15,
                    padding: 2,
                    align: 'center',
                    width: 15,
                    height: 15
                },
                title: {
                    backgroundColor: '#8d7fec',
                    color: '#fff',
                    width: 77,
                    align: 'left',
                    borderRadius: 5,
                    padding: 5,
                }
            }
        },
    }],
    series: [{
        name: '(cal/100g)',
        type: 'bar',
        yAxisIndex: 0,
        data: data,
        barWidth: 10,
        label: {
            normal: {
                show: true,
                position: 'right',
                textStyle: {
                    color: '#333',
                    fontSize: '16',
                }
            }
        },
        itemStyle: {
            normal: {
                barBorderRadius: 20,
                color: function (params) {
                    var num = myColor.length;
                    return myColor[params.dataIndex % num]
                },
                // 渐变色
                // color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
                // offset: 0,
                // color: 'rgba(0,255,0)'
                // }, {
                // offset: 1,
                // color: 'rgb(215 ,255,0)'
                // }]),

            }
        },

    },
    ]
};


// 使用刚指定的配置项和数据显示图表。
myChart.setOption(option);