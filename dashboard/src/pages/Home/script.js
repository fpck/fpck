import PageContent from '@/components/PageContent';
export default {
  components: {
    PageContent
  },
  data: function () {
    return {
      plotData1: [
        {
          x: 1,
          y: 1
        },
        {
          x: 2,
          y: -1
        },
        {
          x: 3,
          y: 2
        }
      ],

      plotData2: [
        {
          x: 1,
          y: -1
        },
        {
          x: 2,
          y: 1
        },
        {
          x: 3,
          y: 2
        }
      ]
    };
  },
  name: 'Home'
};
