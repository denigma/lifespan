// Generated by CoffeeScript 1.6.3
(function() {
  var __hasProp = {}.hasOwnProperty,
    __extends = function(child, parent) { for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; } function ctor() { this.constructor = child; } ctor.prototype = parent.prototype; child.prototype = new ctor(); child.__super__ = parent.prototype; return child; };

  Denigma.BarView = (function(_super) {
    __extends(BarView, _super);

    BarView.prototype.width = void 0;

    BarView.prototype.test = void 0;

    BarView.prototype.control = void 0;

    function BarView(poser, minW, minH) {
      this.minW = minW;
      this.minH = minH;
      BarView.__super__.constructor.call(this, poser);
      this.test = new Denigma.ExperimentBar(this.poser, "test", this.minW, this.minH);
      this.control = new Denigma.ExperimentBar(this.poser, "control", this.minW, this.minH * 3);
    }

    BarView.prototype.append = function(novel) {
      this.control.append(novel);
      return this.test.append(novel);
    };

    BarView.prototype.update = function(sel) {
      this.makeScale(sel);
      this.control.scale = this.scale;
      this.control.update(sel);
      this.test.scale = this.scale;
      return this.test.update(sel);
    };

    BarView.prototype.makeScale = function(sel) {
      var data, max;
      this.width = sel.attr("width");
      data = sel.data();
      max = d3.max(data, function(d) {
        return d.get("max");
      });
      return this.scale = d3.scale.linear().domain([0, max]).range([0, this.width - this.poser.rowMargin]);
    };

    return BarView;

  })(Denigma.BasicView);

}).call(this);
