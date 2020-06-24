var myChart = echarts.init(document.getElementById('c2'));

// 指定图表的配置项和数据
let data1 = {
    xData: ['鲜枣', '黑加仑', '番石榴', '猕猴桃', '山楂', '草莓', '木瓜', '龙眼', '荔枝', '桑葚', '橙子', '柿子', '柑橘', '葡萄', '柚', '芒果', '柠檬', '菠萝', '哈密瓜', '樱桃', '石榴', '杨梅', '菠萝蜜', '枇杷', '香蕉', '桃', '杨桃', '梨', '椰子', '西瓜', '苹果'],
    yData: [243, 181, 68, 62, 53, 47, 43, 43, 41, 38, 33, 30, 28, 25, 23, 23, 22, 18, 12, 10, 9, 9, 9, 8, 8, 7, 7, 6, 6, 6, 4]
}
/**
 双X轴标签对应，伪实现思路：
 底部的标签也是柱状图，对应包含的区域为上方X轴条数占总数的比例，设为宽度即可
 */
option = {
    title: {
        text: '常见水果维生素C含量',
        left: 'center',
        top: "5%",
        textStyle: {
            color: '#fff'
        },
    },
    // grid: {
    //     // top: '20%',
    //     left: '10%'
    //
    // },
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'shadow'
        },
        confine: true,
    },
    grid: [
        {
            // top: '20%',
            left: '15%'

        },
        {
            top: 100,
            bottom: 101
        },
        {
            height: 60,
            bottom: 40
        }
    ],
    xAxis: [{
        type: 'category',
        data: data1.xData,
        gridIndex: 0,
        name: '水果名称',
        nameLocation: 'middle',
        nameGap: 40,
        nameTextStyle: {
            color: '#ffffff',
            fontWeight: 'bold'
        },
        axisLabel: {
            color: '#333',
            interval: 0,
            formatter: function (value) {
                //x轴的文字改为竖版显示
                var str = value.split("");
                return str.join("\n");
            }
        },
        axisLine: {
            lineStyle: {
                color: '#e7e7e7'
            }
        },
        axisTick: {
            lineStyle: {
                color: '#e7e7e7'
            }
        },
        zlevel: 1
    },
        {
            type: 'category',
            gridIndex: 1,
            axisLine: {
                show: false
            },
            zlevel: 1
        }
    ],
    yAxis: [{
        type: 'value',
        gridIndex: 0,
        nameLocation: 'middle',
        nameGap: 40,
        nameRotate: 90,
        name: '维生素含量(mg/100g)',
        color:'white',
        nameTextStyle: {
            color: '#ffffff',
            fontWeight: 'bold'
        },
        axisLabel: {
            color: '#333'
        },
        splitLine: {
            lineStyle: {
                type: 'dashed'
            }
        },
        axisLine: {
            lineStyle: {
                color: '#ccc'
            }
        },
        axisTick: {
            lineStyle: {
                color: '#ccc'
            }
        }
    }, {
        type: 'value',
        gridIndex: 1,
        axisLabel: {
            show: false
        },
        axisLine: {
            show: false
        },
        splitLine: {
            show: false
        },
        axisTick: {
            show: false
        }
    }],
    series: [{
        data: data1.yData,
        type: 'bar',
        label: {
            show: true,
            position: 'top',
            textStyle: {
                color: '#555'//柱状图上数字的颜色
            }
        },
        itemStyle: {
            normal: {
                color: (params) => {
                    let colors = ['#4150d8', '#28bf7e', '#ed7c2f', '#f2a93b', '#f9cf36', '#4a5bdc', '#4cd698', '#f4914e', '#fcb75b', '#ffe180', '#b6c2ff', '#96edc1', '#28bf7e', '#ed7c2f', '#f2a93b', '#f9cf36', '#4a5bdc', '#4cd698', '#f4914e', '#fcb75b', '#ffe180', '#b6c2ff', '#96edc1', '#28bf7e', '#ed7c2f', '#f2a93b', '#f9cf36', '#4a5bdc', '#4cd698', '#f4914e', '#fcb75b', '#ffe180', '#b6c2ff', '#96edc1']
                    return colors[params.dataIndex]
                }
            }
        },
    }]
};

// 使用刚指定的配置项和数据显示图表。
myChart.setOption(option);