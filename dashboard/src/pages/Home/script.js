import PageContent  from "@/components/PageContent";
import LineChart  from "@/components/LineChart";
export default {
  components: {
    PageContent,
    LineChart,
  },
  data: function () {
    return{
      plotData1:[
        {
          x: 1,
          y: 1,
        },
        {
          x: 2,
          y: -1,
        },
        {
          x: 3,
          y: 2,
        },
      ],

      plotData2:[
        {
          x: 1,
          y: -1,
        },
        {
          x: 2,
          y: 1,
        },
        {
          x: 3,
          y: 2,
        },
      ]
    }
  },
  name: 'Home',
}
