var myChart = echarts.init(document.getElementById('echarts2'));


    var seriesData = [{
        name: "香蕉园",
        value: "3"
    }, {
        name: "苹果园",
        value: "18"
    }, {
        name: "柑桔园",
        value: "20"
    }, {
        name: "梨园",
        value: "9"
    }, {
        name: "葡萄园",
        value: "6"
    }, {
        name: "其它",
        value: "44"
    }];
    var legendData = ["香蕉园", "苹果园", "柑桔园", "梨园", "葡萄园", "其它"]
    var colorList = ['#73DDFF', '#73ACFF', '#FDD56A', '#FDB36A', '#FD866A', '#9E87FF', '#58D5FF'];
    option = {
        // backgroundColor: {
        //     type: 'linear',
        //     x: 0,
        //     y: 0,
        //     x2: 1,
        //     y2: 1,
        //     colorStops: [{
        //         offset: 0,
        //         color: '#0f2c70' // 0% 处的颜色
        //     }, {
        //         offset: 1,
        //         color: '#091732' // 100% 处的颜色
        //     }],
        //     globalCoord: false // 缺省为 false
        // },
        // title: {
        //     text: '中国果园面积分布情况',
        //     x: '45%',
        //     y: 'center',
        //     textStyle: {
        //         color: '#fff',
        //         fontSize:10,
        //     }
        // },
        tooltip: {
            trigger: 'item',
            borderColor: 'rgba(255,255,255,.3)',
            backgroundColor: 'rgba(13,5,30,.6)',
            borderWidth: 1,
            padding: 5,
            formatter: function (parms) {
                var str = parms.marker + "" + parms.data.name + "</br>"
                "占比：" + parms.percent + "%";
                return str;
            }
        },
        legend: {
            type: "scroll",
            orient: 'vertical',
            left: '0',
            align: 'auto',
            top: 'middle',
            textStyle: {
                color: 'black'
            },
            data: legendData
        },
        series: [{
            type: 'pie',
            center: ['55%', '50%'],
            radius: ['25%', '45%'],
            clockwise: true,
            avoidLabelOverlap: true,
            hoverOffset: 15,
            itemStyle: {
                normal: {
                    color: function (params) {
                        return colorList[params.dataIndex]
                    }
                }
            },
            label: {
                show: true,
                position: 'outside',
                formatter: '{a|{b}：{d}%}\n{hr|}',
                rich: {
                    hr: {
                        backgroundColor: 't',
                        borderRadius: 3,
                        width: 3,
                        height: 3,
                        padding: [3, 3, 0, -12]
                    },
                    a: {
                        padding: [-30, 15, -20, 15]
                    }
                }
            },
            labelLine: {
                normal: {
                    length: 20,
                    length2: 30,
                    lineStyle: {
                        width: 1
                    }
                }
            },
            data: seriesData
        }]
    };

    // 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);