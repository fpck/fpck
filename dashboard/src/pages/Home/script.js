import PageContent from '@/components/PageContent';
import Plot from '@/components/Plot';
import { QuandlApi } from "@/services/api";
export default {
  components: {
    PageContent,
    Plot
  },
  name: 'Home',
  data: function () {
    return {
      rows:[],
      plotData: [{
        x: [1, 2, 3, 4],
        y: [10, 15, 13, 17],
        type: 'scatter'
      }],
      layout: {
        xaxis: {
          type: 'date'
        },
      },
      code:'FB',
    }
  },
  methods: {
    getPrice: function () {
      const api = new QuandlApi({
        databaseCode: 'WIKI', 
        datasetCode: this.code, 
      });
      api.all()
        .then(res => {
          const data = res.data.dataset_data.data;
          this.plotData = [{
            type: 'scatter',
            x: data.map(x => x[0]),
            y: data.map(x => x[1])
          }];
        });
    }
  } 
};
