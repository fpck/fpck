import PageContent from '@/components/PageContent';
import { QuandlApi } from "@/services/api";
export default {
  components: {
    PageContent
  },
  name: 'Home',
  data: function () {
    return {
      rows:[],
    }
  },
  methods: {
    getPrice: function () {
      const api = new QuandlApi({
        databaseCode: 'WIKI', 
        datasetCode: 'FB', 
      });
      api.all()
        .then(res => {
          console.log(res.data.dataset_data.data);
          this.rows = res.data.dataset_data.data
        });
    }
  } 
};
