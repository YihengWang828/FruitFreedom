var myChart = echarts.init(document.getElementById('c1'));
option = {
    title: {
        text: '中国水果产量区域分布情况',
        subtext: '为什么水果价格存在地区差异',
        left: 'center',
        subtextStyle: {
            color: '#FDF5E6'
        },
        textStyle: {
            color: '#fff'
        },
        // top: "5%",
    },
    // backgroundColor: "white",
    color: ['#2edfa3', '#bce672', '#ff4777', '#70f3ff', '#4b5cc4', '#f47983', '#8d4bbb', '#6635EF', '#FFAFDA'],
    tooltip: {
        trigger: 'item',
        formatter: "地区 <br/>{b}:{d}%",
        confine: true,
    },
    legend: {
        orient: 'horizontal',
        icon: 'circle',
        bottom: 20,
        x: 'center',
        textStyle: {
            color: '#000'
        },
        data: ['东北', '华北', '西北', '西南', '华南', '华中', '华东']
    },
    series: [{
        name: '访问来源',
        type: 'pie',
        selectedMode: 'single',
        radius: [0, '38%'],
        color: ['#2edfa3', '#bce672', '#ff4777', '#FFAFDA', '#4b5cc4', '#f47983', '#8d4bbb', '#6635EF',],
        label: {
            normal: {
                show: false,
                position: 'inner',
                formatter: '{d}%',
                textStyle: {
                    color: '#fff',
                    fontWeight: 'normal',
                    fontSize: 20
                }
            }
        },
        labelLine: {
            normal: {
                show: false
            }
        },
        data: [{
            value: 4.34,
            name: '东北'
        },
            {
                value: 10.56,
                name: '华北'
            },
            {
                value: 16.59,
                name: '西北'
            },
            {
                value: 9.81,
                name: '西南'
            },
            {
                value: 15.23,
                name: '华南'
            },
            {
                value: 17.86,
                name: '华中'
            },
            {
                value: 25.61,
                name: '华东'
            },

        ]
    },
        {
            name: '访问来源',
            type: 'pie',
            radius: ['40%', '42%'],
            label: {
                normal: {
                    formatter: '{b|{b}}\n{hr|}\n{d|{d}%}',
                    rich: {
                        b: {
                            fontSize: 10,
                            // color: '#708090',
                            align: 'left',
                            padding: 4
                        },
                        hr: {
                            borderColor: '#12EABE',
                            width: '100%',
                            borderWidth: 2,
                            height: 0
                        },
                        d: {
                            fontSize: 10,
                            // color: '#D3D3D3',
                            align: 'left',
                            padding: 4
                        },
                        c: {
                            fontSize: 20,
                            color: '#fff',
                            align: 'center',
                            padding: 4
                        }
                    }
                }
            },
            labelLine: {
                normal: {
                    show: true,
                    length: 20,
                    length2: 20,
                    lineStyle: {
                        type: 'dashed',
                        width: 2
                    }
                }
            },
            data: [{
                value: 4.34,
                name: '东北'
            },
                {
                    value: 10.56,
                    name: '华北'
                },
                {
                    value: 16.59,
                    name: '西北'
                },
                {
                    value: 9.81,
                    name: '西南'
                },
                {
                    value: 15.23,
                    name: '华南'
                },
                {
                    value: 17.86,
                    name: '华中'
                },
                {
                    value: 25.61,
                    name: '华东'
                },


            ]
        }
    ]
};

// 使用刚指定的配置项和数据显示图表。
myChart.setOption(option);