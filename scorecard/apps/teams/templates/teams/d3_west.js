/**
 * Created by wew on 12/16/15.
 */

function getTablePrefix(table_id) {

    var prefix = "";

    if (table_id === "product_quality_table") {
        prefix =  "pq";
    } else if (table_id === "quality_assurance_table") {
        prefix = "qa";
    } else if (table_id === "quality_innovation_table") {
        prefix = "qi";
    } else if (table_id === "requirements_engineering_table") {
        prefix = "re";
    } else if (table_id === "test_engineering_table") {
        prefix = "te";
    } else if (table_id === "test_lab_table") {
        prefix = "tl";
    } else {
        alert("Error in 'getTablePrefix' for " + table_id);
    }
    return prefix;
}


function addIdsToMainTable(table_id) {

    var prefix = getTablePrefix(table_id);

    var row_count = 0;
    $('#' + table_id + ' thead tr').each(function () {
        var column_count = 0;
        $('th', this).each(function () {
            var temp_id = prefix + "_" + row_count + "_" + column_count;
            $(this).attr("id", temp_id);
            column_count++;
        });
    });

    row_count = 1;

    $('#' + table_id + ' tbody tr').each(function () {
        var column_count = 0;
        $('td', this).each(function () {
            var temp_id = prefix + "_" + row_count + "_" + column_count;
            $(this).attr("id", temp_id);
            column_count++;
        });
        row_count++;
    })
}

// http://bl.ocks.org/jdarling/06019d16cb5fd6795edf
var randomColor = (function () {
    var golden_ratio_conjugate = 0.618033988749895;
    var h = Math.random();

    var hslToRgb = function (h, s, l) {
        var r, g, b;

        if (s == 0) {
            r = g = b = l; // achromatic
        } else {
            function hue2rgb(p, q, t) {
                if (t < 0) t += 1;
                if (t > 1) t -= 1;
                if (t < 1 / 6) return p + (q - p) * 6 * t;
                if (t < 1 / 2) return q;
                if (t < 2 / 3) return p + (q - p) * (2 / 3 - t) * 6;
                return p;
            }

            var q = l < 0.5 ? l * (1 + s) : l + s - l * s;
            var p = 2 * l - q;
            r = hue2rgb(p, q, h + 1 / 3);
            g = hue2rgb(p, q, h);
            b = hue2rgb(p, q, h - 1 / 3);
        }

        return '#' + Math.round(r * 255).toString(16) + Math.round(g * 255).toString(16) + Math.round(b * 255).toString(16);
    };

    return function () {
        h += golden_ratio_conjugate;
        h %= 1;
        return hslToRgb(h, 0.5, 0.60);
    };
})();

function getParsedDate(temp_date) {

    // Oct 5, 2015, 4:36p.m., only need the month and day
    // or 2015-12-11
    var hyphen_index = temp_date.indexOf("-");

    var temp_array;
    var month;
    var day;

    if (hyphen_index > -1) {
        // parsing the 2015-12-11 format

        temp_array = temp_date.split("-");

        month = temp_array[1];
        day = temp_array[2];

    } else {
        // parsing the old format, Oct 5, 2015

        temp_array = temp_date.split(" ");

        month = temp_array[0];
        day = temp_array[1];

    }

    // hide_columns = hide_columns.replace(/\[/g, '');

    // clean up the month (if present, remove the trailing period)
    month = month.replace(/\./g, '').trim();

    // clean up the day (if present, remove the trailing comma)
    day = day.replace(/\,/g, '').trim();

    return month + "-" + day;
}

// returns a friendly month day, year string for the pie chart
function getParsedMonthDayYear(temp_date) {

    // Oct 5, 2015, 4:36p.m., only need the month and day
    // or 2015-12-11

    var hyphen_index = temp_date.indexOf("-");

    var temp_array;
    var month;
    var day;
    var year;

    if (hyphen_index > -1) {
        // parsing the 2015-12-11 format

        temp_array = temp_date.split("-");

        year = temp_array[0];
        month = temp_array[1];
        day = temp_array[2];

    } else {
        // parsing the old format, Oct 5, 2015

        temp_array = temp_date.split(" ");

        month = temp_array[0];
        day = temp_array[1];
        year = temp_array[2];

    }

    // clean up the month (if present, remove the trailing period)
    month = month.replace(/\./g, '').trim();

    // clean up the day (if present, remove the trailing comma)
    day = day.replace(/\,/g, '').trim();

    // clean up the year (if present, remove the trailing comma)
    year = year.replace(/\,/g, '').trim();

    return month + "/" + day + "/" + year;
}

// given the column number, find the column name
// used to set the label for the charts
function getColumnNameFromColumnDetailsList(column_number, temp_column_details_list) {

    var column_name = "";

    for (var index = 0; index < temp_column_details_list.length; index++) {

        var temp_object = temp_column_details_list[index];
        var temp_column = temp_object.column_number;

        if (parseInt(temp_column, 0) === parseInt(column_number, 10)) {
            column_name = temp_object.header_text;
            break;
        }
    }

    return column_name;
}

// column_details_list
function getFieldTypeByColumnNumber(column_number, temp_column_details_list) {

    var field_type = "";

    for (var index = 0; index < temp_column_details_list.length; index++) {

        var temp_object = temp_column_details_list[index];
        var temp_column = temp_object.column_number;

        if (parseInt(temp_column, 0) === parseInt(column_number, 10)) {
            field_type = temp_object.meta_type;
            break;
        }
    }

    return field_type;
}

function getAllDataMax(temp_all_data) {

    var max = -100000000000000;

    for (var row_index = 0; row_index < temp_all_data.length; row_index++) {

        var temp_array = temp_all_data[row_index];

        // read through each column in the temp_array and find the minimum
        for (var column_index = 0; column_index < temp_array.length; column_index++) {

            var temp_object = temp_array[column_index];
            var temp_value = parseInt(temp_object.DAU, 10);

            if (temp_value > max) {
                max = temp_value;
            }

        }
    }
    return max;
}

function getAllDataMin(temp_all_data) {

    // column 1:  45, 15, 25, 10, 50, 30, 10, 40
    // column 2:   1,  2,  3,  3,  5,  3,  2,  1

    var min = 100000000000000;

    for (var row_index = 0; row_index < temp_all_data.length; row_index++) {

        var temp_array = temp_all_data[row_index];

        // read through each column in the temp_array and find the minimum
        for (var column_index = 0; column_index < temp_array.length; column_index++) {

            var temp_object = temp_array[column_index];
            var temp_value = parseInt(temp_object.DAU, 10);

            if (temp_value < min) {
                min = temp_value;
            }

        }
    }
    return min;
}


function addXAxisColumnDataToBarChart(chart_object) {
    alert("Drag and Drop to the X-Axis for the Bar Chart Has Not Been Implemented.");
}

function addXAxisColumnDataToPieChart(chart_object) {
    alert("Drag and Drop to the X-Axis for the Pie Chart Has Not Been Implemented.");
}

function addYAxisColumnDataToBarChart(chart_object) {
    alert("Drag and Drop to the Y-Axis for the Bar Chart Has Not Been Implemented.");
}

function addYAxisColumnDataToPieChart(chart_object) {
    alert("Drag and Drop to the Y-Axis for the Pie Chart Has Not Been Implemented.");
}

function displayObject(temp_object, message) {

    var hyphens = '------------------------------------------';
    var output = hyphens + '\n';

    if (message !== undefined) {
        output = output + message + "\n" + hyphens + "\n";
    }
    //for (var property in temp_object) {
    //    output += property + ':  ' + temp_object[property] + '\n';
    //}
    //output += hyphens;

    for (var key in temp_object) {
        if (temp_object.hasOwnProperty(key)) {
            output += key + ':  ' + temp_object[key] + '\n';
        }
    }
    output += hyphens;

    alert(output);
}

// replaces the json_data
function get_column_data(temp_column_number, temp_table_id) {

    var column_data = [];

    $('#' + temp_table_id + ' tbody tr').each(function () {
        var temp_data = $(this).children(" td:eq(" + Number(temp_column_number) + ") ").text();
        temp_data = temp_data.replace(/\$/g, '').trim();
        temp_data = temp_data.replace(/\,/g, '').trim();

        column_data.push(temp_data);
    });

    return column_data;
}

function get_date_time_data(temp_date_time_column_number, temp_table_id) {

    var temp_date_time_data = [];

    $('#' + temp_table_id + ' tbody tr').each(function () {
        var temp_date_time_value = $(this).children("td:eq(" + temp_date_time_column_number + ")").text();
        var temp_date = new Date.parse(temp_date_time_value);  // Oct. 5, 2015, 4:36 p.m.
        temp_date_time_data.push(temp_date);
    });

    return temp_date_time_data;
}

// call this to build a list of all of the column names before any are hidden
// it also creates a mapping between the meta data of the model and the table display
// since I need to know what type of data is being dropped into a chart
function buildColumnNamesList(temp_table_id, temp_all_column_names_list, temp_column_data_list_json, temp_column_details_list) {

    // this section maps the table cells ww field to the column_number field
    var ww_field_array = [];
    ww_field_array.push("start_of_week");
    ww_field_array.push("hours");
    ww_field_array.push("weekly_team_size");
    ww_field_array.push("column01");
    ww_field_array.push("column02");
    ww_field_array.push("column03");
    ww_field_array.push("column04");
    ww_field_array.push("column05");
    ww_field_array.push("column06");
    ww_field_array.push("column07");
    ww_field_array.push("column08");
    ww_field_array.push("column09");
    ww_field_array.push("column10");
    ww_field_array.push("column11");
    ww_field_array.push("column12");
    ww_field_array.push("column13");
    ww_field_array.push("column14");
    ww_field_array.push("column15");

    var column_number = 0;

    $("#" + temp_table_id + " tr th").each(function () {
        var header_text = $(this).text();
        temp_all_column_names_list.push(header_text);

        var temp_object = [];
        temp_object.column_number = column_number;
        temp_object.header_text = header_text;
        temp_object.ww_field = ww_field_array[column_number].trim();

        temp_column_details_list.push(temp_object);
        column_number = column_number + 1;
    });

    temp_column_data_list_json = temp_column_data_list_json.replace(/\"/g, '');

    var json_array = temp_column_data_list_json.split("]");

    var cleaned_array = [];

    for (var index = 0; index < json_array.length; index++) {
        var temp = json_array[index];
        temp = temp.replace(/\[/g, '');
        temp = temp.replace(/\]/g, '');

        var comma_index = temp.indexOf(",");

        if (comma_index === 0) {
            temp = temp.substring(1);
            if (temp.indexOf("ForeignKey") > 0) {
            } else {

                var split_array = temp.split(",");

                cleaned_array.push( { 'meta_name': split_array[0].trim(), 'meta_type': split_array[1].trim() } );
            }
        }
    }

    for (var cleaned_index = 0; cleaned_index < cleaned_array.length; cleaned_index++) {

        var temp_object = cleaned_array[cleaned_index];

        var meta_name = temp_object.meta_name;
        var meta_type = temp_object.meta_type;

        // read through the column_details_list and find the object with the matching ww_field
        for (var details_index = 0; details_index < temp_column_details_list.length; details_index++) {
            var temp_details_object = temp_column_details_list[details_index];

            var temp_str = temp_details_object.ww_field;

            if (temp_str == meta_name) {
                temp_column_details_list[details_index].meta_type = meta_type;
            }
        }
    }

}

function getLineChartDates(x_axis, temp_table_id) {
    return get_date_time_data(parseInt(x_axis, 10), temp_table_id);
}

/*
function remove_from_list(temp_list, temp_number) {

    for (var index = 0; index < temp_list.length; index++) {
        if (Number(temp_list[index] == Number(temp_number))) {
            temp_list.splice(index, 1);
            break;
        }
    }
}
*/
// the user clicked the button to change the columns to show or hide in the table
// note, not using the right-click functionality since it had problems with the JQuery DataTables
/*
function showHideColumn(column_number, show_hide, temp_table_id) {

    var oTable = $('#' + temp_table_id).dataTable();

    if (show_hide === "hide") {
        oTable.fnSetColumnVis(column_number, false, false);
    } else if (show_hide === "show") {
        oTable.fnSetColumnVis(column_number, true, false);
    }
    oTable.fnDraw();
}
*/
/*
function hideUserColumnPreferences(temp_table_id, temp_hide_columns_json) {

    var columns = [];

    // this will be empty if the user didn't opt to hide any columns when the table is loaded
    var json_length = Object.keys(columns).length;

    if (json_length > 0) {

        temp_hide_columns_json = temp_hide_columns_json.replace(/\[/g, '');
        temp_hide_columns_json = temp_hide_columns_json.replace(/\]/g, '');
        temp_hide_columns_json = temp_hide_columns_json.replace(/\"/g, '');

        var temp_array = temp_hide_columns_json.split(",");

        var oTable = $('#' + temp_table_id).dataTable();

        for (var index = 0; index < temp_array.length; index++) {
            oTable.fnSetColumnVis(temp_array[index], false, false);
        }
        oTable.fnDraw();
    }
}
*/
function drawD3BarChart(chart_object) {

    var svg_id = chart_object.chart_count;
    var temp_chart_svg_prefix = chart_object.chart_svg_prefix;
    var temp_table_id = chart_object.table_id;

    $("#" + temp_chart_svg_prefix + svg_id).html("");

    var chart_width = 400;
    var chart_height = 400;

    var margin = {top: 20, right: 20, bottom: 30, left: 40};
    var width = chart_width - margin.left - margin.right;
    var height = chart_height - margin.top - margin.bottom;

    var x = d3.scale.ordinal().rangeRoundBands([0, width], .1);

    var y = d3.scale.linear().range([height, 0]);

    var xAxis = d3.svg.axis().scale(x).orient("bottom");

    var yAxis = d3.svg.axis().scale(y).orient("left");  //.ticks(10, "%");

    var y_column = chart_object.dnd_drag_column_number;
    var y_data = get_column_data(y_column, temp_table_id);

    // var y_label = getColumnNameFromColumnDetailsList(y_column, column_details_list);

    // parse the date information for the x-axis
    var x_data = get_column_data(primary_date_time_column, temp_table_id);
    var x_date_time = [];

    for (var index01 = 0; index01 < x_data.length; index01++) {
        x_date_time.push(getParsedDate(x_data[index01]));  // string  Oct 5, 2015, 4:36p.m.
    }

    var data = [];
    for (var index02 = 0; index02 < y_data.length; index02++) {
        data.push({'x': x_date_time[index02], 'y': y_data[index02]});
    }

    var xScale = d3.scale.ordinal()
        .domain(d3.range(data.length))
        .rangeRoundBands([0, chart_width], 0.05);

    var yScale = d3.scale.linear()
        .domain([0, d3.max(data)])
        .range([0, chart_height]);

    var ymax = d3.max(data, function (d) {
        return d.y;
    });

    x.domain(data.map(function (d) {
        return d.x;
    }));

    y.domain([0, d3.max(data, function (d) {
        return d.y;
    })]);

    var svg = d3.select("#" + temp_chart_svg_prefix + svg_id).append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis)
        .attr("font-family", "sans-serif")
        .attr("font-size", "10px");

    svg.append("g")
        .attr("class", "y axis")
        .call(yAxis)
        .append("text")
        .attr("transform", "rotate(-90)");

    for (var index = 0; index < data.length; index++) {

        // var d = data[index];

        svg.selectAll("rect")
            .data(data)
            .enter()
            .append("rect")
            .attr("class", "bar")
            .attr("x", function (d) {
                return x(d.x);
            })
            .attr("width", x.rangeBand())
            .attr("y", function (d) {
                return y(d.y);
            })
            .attr("height", function (d) {
                return height - y(d.y);
            })
            .attr("fill", "blue") // randomColor);
            .on("mouseover", function (d) {
                // get this bar's x/y values, then augment for the tooltip
                var xPosition = parseFloat(d3.select(this).attr("x")) + (xScale.rangeBand() / 2) - 4;
                var yPosition = parseFloat(d3.select(this).attr("y")) + 50;

                // create the tooltip label
                svg.append("text")
                    .attr("id", "tooltip")
                    .attr("x", xPosition)
                    .attr("y", yPosition)
                    .attr("text-anchor", "middle")
                    .attr("font-family", "sans-serif")
                    .attr("font-size", "11px")
                    .attr("font-weight", "bold")
                    .attr("fill", "white")
                    .text(d.y);
            })
            .on("mouseout", function () {
                // remove the tooltip
                d3.select("#tooltip").remove();
            });
    }
}

function drawD3LineChart(chart_object) {

    var svg_id = chart_object.chart_count;
    var temp_chart_svg_prefix = chart_object.chart_svg_prefix;
    var temp_table_id = chart_object.table_id;

    // displayObject(chart_object);

    $("#" + temp_chart_svg_prefix + svg_id).html("");

    var data = [];

    // each of the data objects is attached to a date
    var x_axis = chart_object.x_axis;  // date_time_column
    var x_data = getLineChartDates(x_axis, temp_table_id);

    var y_data = get_column_data(chart_object.dnd_drag_column_number, temp_table_id);

    for (var index = 0; index < y_data.length; index++) {
        data.push({'x': x_data[index], 'y': y_data[index]});
    }

    var chart_width = 400, chart_height = 350;
    var margin = {
        top: 20,
        right: 30,
        bottom: 40,
        left: 50
    };

    // these are graph size settings
    var width = chart_width - margin.left - margin.right;
    var height = chart_height - margin.top - margin.bottom;

    var x_min = x_data[0];
    var x_max = x_data[x_data.length - 1];

    var minObjectValue = parseFloat(d3.min(data, function (d) {
        return d.y;
    }));
    var maxObjectValue = parseFloat(d3.max(data, function (d) {
        return d.y;
    }));

    // create the graph object
    var vis = d3.select("#" + temp_chart_svg_prefix + svg_id).append("svg")
        .data(data)
        .attr("class", "metrics-container")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    var y = d3.scale.linear().domain([minObjectValue - (.1 * minObjectValue), maxObjectValue + (.1 * maxObjectValue)]).range([height, 0]);
    var x = d3.time.scale().domain([x_min, x_max]).range([0, width]);

    var yAxis = d3.svg.axis()
        .scale(y)
        .orient("left")
        .ticks(5);

    var xAxis = d3.svg.axis()
        .scale(x)
        .orient("bottom")
        .tickFormat(d3.time.format("%m-%d"));

    vis.append("g")
        .attr("class", "axis")
        .attr("font-family", "sans-serif")
        .attr("font-size", "12px")
        .call(yAxis);

    vis.append("g")
        .attr("class", "axis")
        .attr("transform", "translate(0," + height + ")")
        .attr("font-family", "sans-serif")
        .attr("font-size", "12px")
        .call(xAxis);

    // add the axes labels
    vis.append("text")
        .attr("class", "axis-label")
        .attr("text-anchor", "end")
        .attr("x", width / 2)
        .attr("y", height + 40);
    //.text('Date');

    vis.append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 0 - margin.left)
        .attr("x", 0 - (height / 2))
        .attr("dy", "1.5em")
        .style("text-anchor", "start")
        .text("Hours");

    var line = d3.svg.line()
        .x(function (d) {
            return x(d["x"]);
        })
        .y(function (d) {
            return y(d["y"]);
        });

    vis.append("svg:path")
        .attr("d", line(data))
        .style("stroke", function () {
            return "#000000";
        })
        .style("fill", "none")
        .style("stroke-width", "2.5");
}


function allow_drop(tableid, event) {
    event.preventDefault();
}

function drag(tableid, event) {
    var target = event.target || event.srcElement;
    alert("718  " + tableid + "  " + target.id);
    //home_dnd_id = target.id;
    event.dataTransfer.setData("text", event.target.id);
}

function drop(tableid, event) {
    event.preventDefault();

    var target = event.target || event.srcElement;
    alert("727  " + tableid + "  " + target.id);

    //var temp_array = home_dnd_id.split("_");
    //var temp_column = temp_array[2];
    //add_chart_to_table_home(event, temp_column);
}

