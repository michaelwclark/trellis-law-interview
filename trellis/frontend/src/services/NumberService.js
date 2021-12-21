import axios from 'axios';

export default class NumberService {
  static async get({number}) {
    const url = `/api/num_to_english`;
    const response = await axios.get(url, { params: { number } });
    return response.data;
  }
}


