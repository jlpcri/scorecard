/**
 * Created by wew on 2/11/16.
 *
 * functions to support charts in teams and users home page
 *
 */

function add_ids_to_teams_table(table_id) {

    var prefix = get_prefix_from_table_id(table_id);

    // qa_th_r0_1
    var row_count = 0;
    $('#' + table_id + ' thead tr').each(function () {
        var column_count = 0;
        $('th', this).each(function () {
            var temp_id = prefix + "_th_r" + row_count + "_" + column_count;
            $(this).attr("id", temp_id);
            column_count++;
        });
    });

    row_count = 1;

    // first row is for YTD Average
    // second row is for YTD Totals
    $('#' + table_id + ' tbody tr:gt(1)').each(function () {
        var column_count = 0;
        $('td', this).each(function () {
            var temp_id = prefix + "_" + row_count + "_" + column_count;
            $(this).attr("id", temp_id);
            column_count++;
        });
        row_count++;
    })
}

function build_column_names_list(temp_table_id, temp_all_column_names_list) {

    $("#" + temp_table_id + " tr th").each(function () {
        var header_text = $(this).text();
        temp_all_column_names_list.push(header_text);
    });

}

// http://bl.ocks.org/jdarling/06019d16cb5fd6795edf
var random_color = (function () {

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

function display_object(temp_object, message) {

    var hyphens = '------------------------------------------';
    var output = hyphens + '\n';

    if (message !== undefined) {
        output = output + message + "\n" + hyphens + "\n";
    }

    for (var key in temp_object) {
        if (temp_object.hasOwnProperty(key)) {
            output += key + ':  ' + temp_object[key] + '\n';
        }
    }
    output += hyphens;

    alert(output);
}

// display the elements of an array in separate lines
function display_array(temp_list, message) {

    var hyphens = '------------------------------------------';
    var output = hyphens + '\n';

    if (message !== undefined) {
        output = output + message + "\n" + hyphens + "\n";
    }

    for (var index = 0; index < temp_list.length; index++) {
        output = output + temp_list[index] + "\n";
    }

    output = output + "\n--------------------------";

    alert(output);
}

var dnd_id;

function allow_drop(event) {
    event.preventDefault();
}

function drag(event) {

    var target = event.target || event.srcElement;
    dnd_id = target.id;
    event.dataTransfer.setData("text", event.target.id);
}

function drop(event) {

    event.preventDefault();

    var temp_array = dnd_id.split("_");

    // 0 = prefix, 1 = row (0 based), 2 = column (1 based)
    var prefix = temp_array[0];
    var column = temp_array[2];

    var number_of_charts = $("#" + prefix + "_chart_row").children('td').length;

    // only four charts are allowed per page
    if (number_of_charts >= 4) {
        alert("Only Four Charts Are Allowed.");
    } else {
        add_chart_to_table(event, prefix, column);
    }

}

function add_chart_to_table(event, temp_prefix, temp_column) {

    event.preventDefault();

    var next_chart_id;
    var dnd_charts_list;

    if (temp_prefix === "qah") {

        next_chart_id = home_qa_next_chart_id++;
        dnd_charts_list = home_qa_dnd_charts_list;

    } else if (temp_prefix === "qih") {

        next_chart_id = home_qi_next_chart_id++;
        dnd_charts_list = home_qi_dnd_charts_list;

    } else if (temp_prefix === "reh") {

        next_chart_id = home_re_next_chart_id++;
        dnd_charts_list = home_re_dnd_charts_list;


    } else if (temp_prefix === "teh") {

        next_chart_id = home_te_next_chart_id++;
        dnd_charts_list = home_te_dnd_charts_list;

    } else if (temp_prefix === "tlh") {

        next_chart_id = home_tl_next_chart_id++;
        dnd_charts_list = home_tl_dnd_charts_list;

    } else if (temp_prefix === "qa") {

        next_chart_id = quality_assurance_next_chart_id++;
        dnd_charts_list = quality_assurance_dnd_charts_list;

    } else if (temp_prefix === "qi") {

        next_chart_id = quality_innovation_next_chart_id++;
        dnd_charts_list = quality_innovation_dnd_charts_list;

    } else if (temp_prefix === "re") {

        next_chart_id = requirements_engineering_next_chart_id++;
        dnd_charts_list = requirements_engineering_dnd_charts_list;

    } else if (temp_prefix === "te") {

        next_chart_id = test_engineering_next_chart_id++;
        dnd_charts_list = test_engineering_dnd_charts_list;

    } else if (temp_prefix === "tl") {

        next_chart_id = test_lab_next_chart_id++;
        dnd_charts_list = test_lab_dnd_charts_list;

    }

    var chart_count = next_chart_id;

    var chart_object = new Object();

    chart_object.table_dnd_id = get_table_id_from_prefix(temp_prefix);
    chart_object.chart_count = chart_count;
    chart_object.chart_type = "bar";
    chart_object.x_axis = 0;

    var table_friendly_name = get_drag_table_friendly_name(temp_prefix);
    var column_name = get_y_column_name(chart_object.table_dnd_id, temp_column);
    chart_object.y_column_name = column_name;
    chart_object.chart_title = table_friendly_name + " --- " + column_name;

    // this only applies to tabs on the home page
    if (temp_prefix === "qah" || temp_prefix === "qih" || temp_prefix === "reh" || temp_prefix === "teh" || temp_prefix === "tlh") {
        chart_object.dnd_drag_column_number = get_y_column_number(chart_object.table_dnd_id, column_name);
    } else {
        chart_object.dnd_drag_column_number = temp_column;
    }

    dnd_charts_list.push(chart_object);

    var chart_row_id = get_chart_row_id_from_id(temp_prefix);

    $.ajax({
        url: "{% url 'users:add_home_chart' %}",
        dataType: 'html',
        data: '',
        type: 'POST',
        success: function () {

            var chart_html = get_chart_html(temp_prefix, chart_count);

            $("#" + chart_row_id).append(chart_html);

            draw_flot_bar_chart(chart_object);

            $("input:radio[name='" + temp_prefix + "_chart_group_" + chart_count + "'][value='bar']").prop('checked', true);
            $("#" + temp_prefix + "_chart_title_" + chart_count).html(chart_object.chart_title);

            // alert("Success");
        },
        error: function () {
            alert("Error Adding Chart");
        }
    });
}

function get_drag_table_friendly_name(temp_prefix) {

    var table_name = "";

    if (temp_prefix === "qah" || temp_prefix === "qa") {
        table_name = "Quality Assurance";
    } else if (temp_prefix === "qih" || temp_prefix === "qi") {
        table_name = "Quality Innovation";
    } else if (temp_prefix === "reh" || temp_prefix === "re") {
        table_name = "Requirements Engineering";
    } else if (temp_prefix === "teh" || temp_prefix === "te") {
        table_name = "Test Engineering";
    } else if (temp_prefix === "tlh" || temp_prefix === "tl") {
        table_name = "Test Lab";
    }
    return table_name;
}

function get_y_column_name(temp_table_id, temp_column_number) {

    var prefix = get_prefix_from_table_id(temp_table_id);

    // header id will look like 'pq_th_r1__column
    var temp_id = "#" + prefix + "_th_r0_" + temp_column_number;
    var header_text = $(temp_id).text();

    return header_text;
}

function get_prefix_from_table_id(temp_table_id) {

    var prefix = "";

    if (temp_table_id === "home_quality_assurance_table") {
        prefix = "qah";
    } else if (temp_table_id === "home_quality_innovation_table") {
        prefix = "qih";
    } else if (temp_table_id === "home_requirements_engineering_table") {
        prefix = "reh";
    } else if (temp_table_id === "home_test_engineering_table") {
        prefix = "teh";
    } else if (temp_table_id === "home_test_lab_table") {
        prefix = "tlh";
    } else if (temp_table_id === "quality_assurance_table") {
        prefix = "qa";
    } else if (temp_table_id === "quality_innovation_table") {
        prefix = "qi";
    } else if (temp_table_id === "requirements_engineering_table") {
        prefix = "re";
    } else if (temp_table_id === "test_engineering_table") {
        prefix = "te";
    } else if (temp_table_id === "test_lab_table") {
        prefix = "tl";
    }

    return prefix;
}

function get_table_id_from_prefix(temp_prefix) {

    // a prefix ending witn an 'h' is from the users home page, otherwise it is from a page in the teams app

    var table_id = "";

    if (temp_prefix === "qah") {
        table_id = "home_quality_assurance_table";
    } else if (temp_prefix === "qih") {
        table_id = "home_quality_innovation_table";
    } else if (temp_prefix === "reh") {
        table_id = "home_requirements_engineering_table";
    } else if (temp_prefix === "teh") {
        table_id = "home_test_engineering_table";
    } else if (temp_prefix === "tlh") {
        table_id = "home_test_lab_table";
    } else if (temp_prefix === "qa") {
        table_id = "quality_assurance_table";
    } else if (temp_prefix === "qi") {
        table_id = "quality_innovation_table";
    } else if (temp_prefix === "re") {
        table_id = "requirements_engineering_table";
    } else if (temp_prefix === "te") {
        table_id = "test_engineering_table";
    } else if (temp_prefix === "tl") {
        table_id = "test_lab_table";
    }

    return table_id;
}

function get_chart_row_id_from_id(temp_prefix) {

    // a prefix ending witn an 'h' is from the users home page, otherwise it is from a page in the teams app

    var chart_row_id = "";

    if (temp_prefix === "qah") {
        chart_row_id = "qah_chart_row";
    } else if (temp_prefix === "qih") {
        chart_row_id = "qih_chart_row";
    } else if (temp_prefix === "reh") {
        chart_row_id = "reh_chart_row";
    } else if (temp_prefix === "teh") {
        chart_row_id = "teh_chart_row";
    } else if (temp_prefix === "tlh") {
        chart_row_id = "tlh_chart_row";
    } else if (temp_prefix === "qa") {
        chart_row_id = "qa_chart_row";
    } else if (temp_prefix === "qi") {
        chart_row_id = "qi_chart_row";
    } else if (temp_prefix === "re") {
        chart_row_id = "re_chart_row";
    } else if (temp_prefix === "te") {
        chart_row_id = "te_chart_row";
    } else if (temp_prefix === "tl") {
        chart_row_id = "tl_chart_row";
    }

    return chart_row_id;
}

function get_chart_html(temp_prefix, temp_chart_count) {

    var output = "<td id='" + temp_prefix + "_chart_td_" + temp_chart_count + "'>";

    output = output + "<table class='chart_dnd_table'><tbody>";

    output = output + "<tr><td id='" + temp_prefix + "_chart_title_" + temp_chart_count + "' class='td_title'></td></tr>";

    output = output + "<tr><td class='chart_td' colspan='2'>";
    output = output + "<div id='" + temp_prefix + "_chart_svg_" + temp_chart_count + "' class='chart_svg_div'></div>";
    output = output + "</td></tr>";

    output = output + "<tr><td colspan='2'>";
    output = output + "<div id='" + temp_prefix + "_radio_div_" + temp_chart_count + "' class='chart_radio_div'>";

    output = output + "<table class='radio_table'><tbody><tr>";
    output = output + "<td><input type='radio' id='" + temp_prefix + "_bar_" + temp_chart_count + "' name='" + temp_prefix + "_chart_group_" + temp_chart_count + "' value='bar' onchange='process_radio_chart_selection(event)'>Bar Chart</td>";
    output = output + "<td><input type='radio' id='" + temp_prefix + "_line_" + temp_chart_count + "' name='" + temp_prefix + "_chart_group_" + temp_chart_count + "' value='line' onchange='process_radio_chart_selection(event)'>Line Chart</td>";
    output = output + "<td><input type='radio' id='" + temp_prefix + "_pie_" + temp_chart_count + "' name='" + temp_prefix + "_chart_group_" + temp_chart_count + "' value='pie' onchange='process_radio_chart_selection(event)'>Pie Chart</td>";

    output = output + "<td class='td_delete_btn'><input type='button' id='" + temp_prefix + "_delete_chart_button_" + temp_chart_count + "' value='Delete Chart' onclick='on_click_delete_chart(event)'></td>";
    output = output + "</table></div>";

    output = output + "</td></tr>";

    output = output + "</tbody></table></td>";

    // alert(output);

    return output;
}

function process_radio_chart_selection(event) {

    var target = event.target || event.srcElement;
    var target_id = target.id;

    var details_list = target_id.split("_");

    var prefix = details_list[0];
    var new_chart_type = details_list[1];
    var chart_count = details_list[2];

    var chart_object = get_chart_object_from_list(prefix, chart_count);

    if (chart_object === null || chart_object === undefined) {

        alert("Error 931: Could not find chart");

    } else {

        if (new_chart_type === 'bar') {

            chart_object.chart_type = "bar";
            draw_flot_bar_chart(chart_object);

        } else if (new_chart_type === 'line') {

            chart_object.chart_type = "line";
            draw_flot_line_chart(chart_object);

        } else if (new_chart_type === 'pie') {

            chart_object.chart_type = "pie";
            draw_flot_pie_chart(chart_object);

        } else {
            alert("Unsupported Chart Type.");
        }

    }
}

function on_click_delete_chart(event) {

    var target = event.target || event.srcElement;
    var target_id = target.id;

    var temp_array = target_id.split("_");
    var prefix = temp_array[0];

    var chart_id = temp_array[temp_array.length - 1];

    $.ajax({
        url: "{% url 'users:delete_home_chart' %}",
        dataType: 'html',
        data: '',
        type: 'POST',
        success: function (data) {
            $("#" + prefix + "_chart_td_" + chart_id).remove();
            remove_chart_from_list(prefix, chart_id);
        },
        error: function (data, status, error) {
            alert("Error Deleting Chart " + status);
        }
    });

}

function remove_chart_from_list(temp_prefix, temp_number) {

    var dnd_charts_list;

    if (temp_prefix === "qah") {
        dnd_charts_list = home_qa_dnd_charts_list;
    } else if (temp_prefix === "qih") {
        dnd_charts_list = home_qi_dnd_charts_list;
    } else if (temp_prefix === "reh") {
        dnd_charts_list = home_re_dnd_charts_list;
    } else if (temp_prefix === "teh") {
        dnd_charts_list = home_te_dnd_charts_list;
    } else if (temp_prefix === "tlh") {
        dnd_charts_list = home_tl_dnd_charts_list;
    } else if (temp_prefix === "qa") {
        dnd_charts_list = quality_assurance_dnd_charts_list;
    } else if (temp_prefix === "qi") {
        dnd_charts_list = quality_innovation_dnd_charts_list;
    } else if (temp_prefix === "re") {
        dnd_charts_list = requirements_engineering_dnd_charts_list;
    } else if (temp_prefix === "te") {
        dnd_charts_list = test_engineering_dnd_charts_list;
    } else if (temp_prefix === "tl") {
        dnd_charts_list = test_lab_dnd_charts_list;
    }

    for (var index = 0; index < dnd_charts_list.length; index++) {
        var temp_object = dnd_charts_list[index];
        if (temp_object.chart_count == temp_number) {
            dnd_charts_list.splice(index, 1);
            break;
        }
    }
}

function get_chart_object_from_list(temp_prefix, temp_chart_count) {

    var dnd_charts_list;

    if (temp_prefix === "qah") {
        dnd_charts_list = home_qa_dnd_charts_list;
    } else if (temp_prefix === "qih") {
        dnd_charts_list = home_qi_dnd_charts_list;
    } else if (temp_prefix === "reh") {
        dnd_charts_list = home_re_dnd_charts_list;
    } else if (temp_prefix === "teh") {
        dnd_charts_list = home_te_dnd_charts_list;
    } else if (temp_prefix === "tlh") {
        dnd_charts_list = home_tl_dnd_charts_list;
    } else if (temp_prefix === "qa") {
        dnd_charts_list = quality_assurance_dnd_charts_list;
    } else if (temp_prefix === "qi") {
        dnd_charts_list = quality_innovation_dnd_charts_list;
    } else if (temp_prefix === "re") {
        dnd_charts_list = requirements_engineering_dnd_charts_list;
    } else if (temp_prefix === "te") {
        dnd_charts_list = test_engineering_dnd_charts_list;
    } else if (temp_prefix === "tl") {
        dnd_charts_list = test_lab_dnd_charts_list;
    }

    var chart_object = null;

    for (var index = 0; index < dnd_charts_list.length; index++) {
        var temp_object = dnd_charts_list[index];

        if (Number(temp_object.chart_count) == Number(temp_chart_count)) {
            chart_object = temp_object;
            break;
        }
    }
    return chart_object;
}

function draw_flot_bar_chart(chart_object) {

    var prefix = get_prefix_from_table_id(chart_object.table_dnd_id);

    var svg_id = chart_object.chart_count;
    var chart_id = "#" + prefix + "_chart_svg_" + svg_id;

    $(chart_id).html("");

    var data = [];

    var table_id = chart_object.table_dnd_id;

    var weekly_data = get_column_data(0, table_id);

    var parsed_date_list = [];

    for (var index01 = 0; index01 < weekly_data.length; index01++) {
        parsed_date_list.push(get_parsed_month_day(weekly_data[index01]));  // string  Oct 5, 2015, 4:36p.m.
    }
    parsed_date_list.reverse();

    var chart_data = get_column_data(chart_object.dnd_drag_column_number, table_id);
    chart_data.reverse();

    for (var index = 0; index < chart_data.length; index++) {
        data.push({data: [[parsed_date_list[index], chart_data[index]]], color: random_color()});
    }

    data.reverse();

    var temp_width = 75 * data.length;
    $('.chart_td').css("width", temp_width + 'px');
    $(chart_id).css("width", temp_width + 'px');

    $.plot(chart_id, data, {
        series: {
            bars: {
                show: true,
                barWidth: 0.9,
                align: "center",
                lineWidth: 0,
                fill: 1.0
            }
        },
        xaxis: {
            mode: "categories",
            tickLength: 0
        }
    });
}

function draw_flot_line_chart(chart_object) {

    var prefix = get_prefix_from_table_id(chart_object.table_dnd_id);

    var svg_id = chart_object.chart_count;
    var chart_id = "#" + prefix + "_chart_svg_" + svg_id;

    $(chart_id).html("");

    var data = [];

    var table_id = chart_object.table_dnd_id;

    var weekly_data = get_column_data(0, table_id);

    var parsed_date_list = [];

    for (var index01 = 0; index01 < weekly_data.length; index01++) {
        parsed_date_list.push(get_parsed_month_day(weekly_data[index01]));  // string  Oct 5, 2015, 4:36p.m.
    }

    var chart_data = get_column_data(chart_object.dnd_drag_column_number, table_id);

    for (var index = 0; index < chart_data.length; index++) {
        data.push([parsed_date_list[index], chart_data[index]]);
    }

    var temp_width = 75 * data.length;
    $('.chart_td').css("width", temp_width + 'px');
    $(chart_id).css("width", temp_width + 'px');

    $.plot(chart_id, [data], {
        colors: ['black'],
        xaxis: {
            mode: "categories",
            tickLength: 0
        }
    });

}

function draw_flot_pie_chart(chart_object) {

    var prefix = get_prefix_from_table_id(chart_object.table_dnd_id);

    var svg_id = chart_object.chart_count;
    var chart_id = "#" + prefix + "_chart_svg_" + svg_id;

    $(chart_id).html("");

    var data = [];

    var table_id = chart_object.table_dnd_id;

    var weekly_data = get_column_data(0, table_id);

    var parsed_date_list = [];

    for (var index01 = 0; index01 < weekly_data.length; index01++) {
        parsed_date_list.push(get_parsed_month_day_year(weekly_data[index01]));  // string  Oct 5, 2015, 4:36p.m.
    }

    var chart_data = get_column_data(chart_object.dnd_drag_column_number, table_id);

    for (var index = 0; index < chart_data.length; index++) {
        data.push({"label": weekly_data[index], "data": chart_data[index], "color": random_color()});
    }

    data.reverse();

    $('.chart_td').css("width", '400px');
    $(chart_id).css("width", '400px');

    $.plot($(chart_id), data, {
        series: {
            pie: {
                show: true
            }
        },
        grid: {
            hoverable: true,
            clickable: true
        },
        legend: {
            show: false
        }
    });

}

function get_column_data(temp_column_number, temp_table_id) {

    var column_data = [];

    $('#' + temp_table_id + ' tbody tr').each(function () {
        var temp_data = $(this).children(" td:eq(" + Number(temp_column_number) + ") ").text();

        temp_data = temp_data.replace(/\$/g, '').trim();
        temp_data = temp_data.replace(/\,/g, '').trim();

        column_data.push(temp_data);
    });

    var prefix = get_prefix_from_table_id(temp_table_id);

    if (prefix === "qa" || prefix === "qi" || prefix === "re" || prefix === "te" || prefix === "tl") {
        // remove the first two entries since that are YTD Average and YTD Totals
        column_data.splice(0, 2);
    }

    return column_data;
}

// returns a friendly month day, year string
function get_parsed_month_day_year(temp_date) {

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

function get_parsed_month_day(temp_date) {

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

    // clean up the month (if present, remove the trailing period)
    month = month.replace(/\./g, '').trim();

    // clean up the day (if present, remove the trailing comma)
    day = day.replace(/\,/g, '').trim();

    return month + "/" + day;
}

// if the user has hidden some columns, the visible column index and the drag column index will not match
function get_y_column_number(temp_table_id, temp_column_name) {

    var prefix = get_prefix_from_table_id(temp_table_id);
    var temp_all_column_names_list = [];

    if (prefix === "qah") {
        temp_all_column_names_list = home_qa_all_column_names_list;
    } else if (prefix === "qih") {
        temp_all_column_names_list = home_qi_all_column_names_list;
    } else if (prefix === "reh") {
        temp_all_column_names_list = home_re_all_column_names_list;
    } else if (prefix === "teh") {
        temp_all_column_names_list = home_te_all_column_names_list;
    } else if (prefix === "tlh") {
        temp_all_column_names_list = home_tl_all_column_names_list;
    }

    var column_number = -1;

    var visible_column_names_list = [];

    $('#' + prefix + '_th_r1 th').each(function () {

        if ($(this).is(':visible')) {
            var name = $(this).text().trim();

            if ($.inArray(name, visible_column_names_list) == -1) {
                visible_column_names_list.push(name);
            }
        }
    });

    for (var index = 0; index < visible_column_names_list.length; index++) {

        var temp_value = visible_column_names_list[index];

        if (temp_value.trim() === temp_column_name.trim()) {
            column_number = index;
            break;
        }
    }

    return column_number;
}

