import axios from "axios";

export class QuandlApi {
  constructor({databaseCode, datasetCode}) {
    this.url  = 'https://www.quandl.com/api/v3/datasets';
    this.databaseCode = databaseCode;
    this.datasetCode = datasetCode;
  }

  all(){
    const url = `${this.url}/${this.databaseCode}/${this.datasetCode}/data.json`
    return this._get(url, {});
  }
  _get (url, params){
    return axios.get(url, {params: params});
  }
};
