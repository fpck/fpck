import PageContent from '@/components/PageContent';
import { GoogleFinanceApi } from "@/services/api";
export default {
  components: {
    PageContent
  },
  name: 'Home',
  methods: {
    getPrice: function () {
      console.log('aaa');
      console.log(GoogleFinanceApi);
      const api = new GoogleFinanceApi({
        exchange: 'TYO', 
        period: '1Y', 
        interval: 86400, 
        code: 7203 
      });
      api.all();
    }
  } 
};
