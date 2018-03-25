import Plotly from 'plotly.js';

export default {
  props: {
    data: {
      type: Array,
      required: true
    },
    layout: {},
    option: {
      type: Object,
      default: function () {
        return {
          modeBarButtonsToRemove: [
            'sendDataToCloud',
            'hoverCompareCartesian'
          ]
        };
      }
    },
    data: {
      selectedPoints: []
    },
    elementClick: {
      type: Function
    },
    elementDoubleClick: {
      type: Function
    },
    onSelect: {
      type: Function
    }
  },
  methods: {
    newPlot: function () {
      Plotly.newPlot(
        this.$el,
        this.data,
        this.layout,
        this.option
      );
      if (this.elementClick) {
        this.$el.on('plotly_click', (e) => this.elementClick(e));
      }

      if (this.elementDoubleClick) {
        this.$el.on('plotly_doubleclick', (e) => this.elementDoubleClick(e));
      }

      if (this.onSelect) {
        this.$el.on('plotly_selected', (e) => this.onSelect(e));
      }
    },

    redraw: function () {
      Plotly.purge(this.$el);
      this.newPlot();
    },

    handleResize: function () {
      this.redraw();
    }
  },

  watch: {
    data: function (oldValue, newValue) {
      this.redraw();
    },

    option: function (oldValue, newValue) {
      this.redraw();
    },

    layout: function (oldValue, newValue) {
      this.redraw();
    }
  },

  beforeDestroy: function () {
    window.removeEventListener('resize', this.handleResize);
  },

  mounted: function () {
    this.newPlot();
    window.addEventListener('resize', this.handleResize);
  }
};
