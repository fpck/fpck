import axios from "axios";


export class GoogleFinanceApi {
  constructor({exchange, period, interval, code}) {
    this.url  = 'https://www.google.com/finance/getprices';
    this.period = period;
    this.interval = interval;
    this.code = code;
    this.exchange = exchange;
  }

  all(){
    const params = {
      p: this.period,
      i: this.interval,
      x: this.exchange,
      q: this.code
    }
    return this._get(this.url, params);
  }
  _get (url, params){
    return axios.post(url, {params: params});
  }
};
