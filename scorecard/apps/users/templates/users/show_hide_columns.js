/**
 * Created by wew on 2/10/16.
 */

function initialize_metrics_table(table_id, prefix) {

    $("#" + table_id).DataTable({
        "scrollY": 300,
        "scrollX": true,
        "scrollCollapse": true,
        "paging": false,
        "searching": false,
        "info": false,
        "bAutoWidth": true,
        "bSort": false,
        "order": [],
        "fnAdjustColumnSizing": false,
        "fnInitComplete": add_ids_to_metrics_table(table_id)
    });
}

function add_ids_to_metrics_table(table_id) {

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

function on_click_show_hide_columns_dialog(event) {

    var target = event.target || event.srcElement;
    var target_id = target.id;

    var temp_array = target_id.split("_");  // e.g.  qa_show_hide_dialog_button"

    var prefix = temp_array[0];

    var table_id = "";
    var all_column_names_list = [];
    var hide_column_list = [];
    var table_title = "";

    if (prefix == "qah") {

        table_id = home_qa_table_id;
        all_column_names_list = home_qa_all_column_names_list;
        hide_column_list = home_qa_hide_column_list;
        table_title = "Quality Assurance Columns";

    } else if (prefix == "qi") {

        table_id = home_qi_table;
        all_column_names_list = home_qi_all_column_names_list;
        hide_column_list = home_qi_hide_column_list;
        table_title = "Quality Innovation Columns";

    } else if (prefix == "re") {

        table_id = home_re_table_id;
        all_column_names_list = home_re_all_column_names_list;
        hide_column_list = home_re_hide_column_list;
        table_title = "Requirements Engineering Columns";

    } else if (prefix == "te") {

        table_id = home_te_table_id;
        all_column_names_list = home_te_all_column_names_list;
        hide_column_list = home_te_hide_column_list;
        // table_visible = $('#test_engineering_table').is(':visible');
        table_title = "Test Engineering Columns";

    } else if (prefix == "tl") {

        table_id = home_tl_table_id;
        all_column_names_list = home_tl_all_column_names_list;
        hide_column_list = home_tl_hide_column_list;
        table_title = "Test Lab Columns";
    }

    // display_array(all_column_names_list);
    // display_array(hide_column_list);

    var output = "";
    var header_count = 1;

    for (var index = 0; index < all_column_names_list.length; index++) {

        var checkbox_id = prefix + "_column_" + header_count.toString();
        var checkbox_str = "";

        if (index == 0) {
            checkbox_str = "<input type='checkbox' id='" + checkbox_id + "'" + " checked disabled />&nbsp;&nbsp;" + all_column_names_list[index];
        } else {
            checkbox_str = "<input type='checkbox' id='" + checkbox_id + "' + onchange='checkbox_change(event)' />&nbsp;&nbsp;" + all_column_names_list[index];
        }

        output = output + checkbox_str + "<br>";
        header_count++;
    }

    $("#" + prefix + "_west_dialog").dialog({
        title: table_title,
        resizable: false,
        height: 400,
        width: 400,
        modal: false,
        buttons: {
            Close: function () {
                $(this).dialog("close");
            }
        }
    }).html(output);

    var current_column_names_list = [];
    var column_count = 0;

    $('#' + prefix + '_th_r1 th').each(function () {

        var name = $(this).text().trim();
        if ($.inArray(name, current_column_names_list) == -1) {
            current_column_names_list.push(name);
        }
        column_count++;

    });

    for (var index = 0; index < all_column_names_list.length; index++) {

        var in_current = $.inArray(all_column_names_list[index].trim(), current_column_names_list);

        var column_id = prefix + "_column_" + Number(index + 1);

        if (in_current > -1) {
            $("#" + column_id).prop('checked', true);
        } else {
            $("#" + column_id).prop('checked', false);

            if ($.inArray(Number(index + 1), hide_column_list) == -1) {
                hide_column_list.push(Number(index + 1));
            }
        }

    }

}

function checkbox_change(event) {

    var target = event.target || event.srcElement;
    var target_id = target.id;  // column_XX

    var temp_array = target_id.split("_");  // e.g.  qa_show_hide_dialog_button"

    // display_array(temp_array);

    var prefix = temp_array[0];
    var column_number = temp_array[2];

    var checkbox_number = Number(column_number) - 1;  // target_id.substring(column_number + 1)) - 1;

    var checked = $("#" + target_id).prop('checked');

    var table_id = "";
    var hide_column_list = [];
    var max_columns = 0;

    if (prefix == "qah") {

        table_id = home_qa_table_id;
        hide_column_list = home_qa_hide_column_list;
        max_columns = home_qa_all_column_names_list.length;

    } else if (prefix == "qih") {

        table_id = home_qi_table_id;
        hide_column_list = home_qi_hide_column_list;
        max_columns = home_qi_all_column_names_list.length;

    } else if (prefix == "reh") {

        table_id = home_re_table_id;
        hide_column_list = home_re_hide_column_list;
        max_columns = home_re_all_column_names_list.length;

    } else if (prefix == "teh") {

        table_id = home_te_table_id;
        hide_column_list = home_te_hide_column_list;
        max_columns = home_te_all_column_names_list.length;

    } else if (prefix == "tlh") {

        table_id = home_tl_table_id;
        hide_column_list = home_tl_hide_column_list;
        max_columns = home_tl_all_column_names_list.length;

    }

    if (checked) {

        // if the user has checked one of the checkboxes, make sure the checkbox to show/hide the table is correct
        remove_from_hide_list(hide_column_list, checkbox_number);

        show_hide_column(table_id, checkbox_number, "show", false, true);

    } else {

        if ($.inArray(checkbox_number, hide_column_list) == -1) {
            hide_column_list.push(checkbox_number);
        }

        var force_table_hide = false;

        if (hide_column_list.length == max_columns) {
            force_table_hide = true;
        }

        show_hide_column(table_id, checkbox_number, "hide", force_table_hide, false);
    }

    update_hidden_columns_list_db_by_column_name(table_id, hide_column_list);

}

function remove_from_hide_list(temp_list, temp_number) {

    for (var index = 0; index < temp_list.length; index++) {

        if (Number(temp_list[index] == Number(temp_number))) {
            temp_list.splice(index, 1);
            break;
        }
    }

}

function show_hide_column(temp_table_id, column_number, show_hide, force_table_hide, force_table_show) {

    // console.log("show_hide_column " + column_number + "  " + force_table_hide + "  " + force_table_show);

    var oTable = $('#' + temp_table_id).dataTable();

    var prefix = "";
    var max_columns = 0;


    if (temp_table_id === "home_quality_assurance_table") {

        prefix = "qah";
        max_columns = home_qa_all_column_names_list.length;

    } else if (temp_table_id === "home_quality_innovation_table") {

        prefix = "qih";
        max_columns = home_qi_all_column_names_list.length;

    } else if (temp_table_id === "home_requirements_engineering_table") {

        prefix = "reh";
        max_columns = home_re_all_column_names_list.length;

    } else if (temp_table_id === "home_test_engineering_table") {

        prefix = "teh";
        max_columns = home_te_all_column_names_list.length;

    } else if (temp_table_id === "home_test_lab_table") {

        prefix = "tlh";
        max_columns = home_tl_all_column_names_list.length;

    }

    if (show_hide === "hide") {

        if (force_table_hide) {

            // hide the header for the column
            $('#' + prefix + "_th_r1_" + column_number).hide();

            // the fnSetColumnVis call does not remove the whole table if the last column is removed
            $('#td_' + temp_table_id).hide();

            $('#' + prefix + '_th_r1').hide();  // eg.  pq_th_r1

        }

        oTable.fnSetColumnVis(Number(column_number), false, false);

    } else if (show_hide === "show") {  // working here

        // alert("1573  " + force_table_show);

        if (force_table_show) {

            // show the header for the column
            $('#' + prefix + "_th_r1_" + column_number).show();

            $('#td_' + temp_table_id).show();

            $('#' + prefix + '_th_r1').show();  // eg.  pq_th_r1

            // columns in the table body are fine, missing a table header
            oTable.fnSetColumnVis(Number(column_number), true, true);

        }

        // columns in the table body are fine, missing a table header
        for (var index = 0; index < max_columns; index++) {
            $('#' + prefix + "_th_r1_" + (index + 1)).show();
        }

        oTable.fnSetColumnVis(Number(column_number), true, false);

    }

    oTable.fnDraw();

}

function update_hidden_columns_list_db_by_column_name(temp_table_id, temp_id_hide_column_list) {

    var temp_all_column_names_list;
    var table_name = "";

    // rather than change the name in the view.py method, change the table name here
    if (temp_table_id === "home_quality_assurance_table") {
        table_name = "quality_assurance_table";
        temp_all_column_names_list = home_qa_all_column_names_list;
    } else if (temp_table_id === "home_quality_innovation_table") {
        table_name = "quality_innovation_table";
        temp_all_column_names_list = home_qi_all_column_names_list;
    } else if (temp_table_id === "home_requirements_engineering_table") {
        table_name = "requirements_engineering_table";
        temp_all_column_names_list = home_re_all_column_names_list;
    } else if (temp_table_id === "home_test_engineering_table") {
        table_name = "test_engineering_table";
        temp_all_column_names_list = home_te_all_column_names_list;
    } else if (temp_table_id === "home_test_lab_table") {
        table_name = "test_lab_table";
        temp_all_column_names_list = home_tl_all_column_names_list;
    }

    var temp_hidden_names_list = [];

    for (var index = 0; index < temp_id_hide_column_list.length; index++) {

        var temp_value = temp_id_hide_column_list[index];
        var column_name = temp_all_column_names_list[temp_value];

        if ($.inArray(column_name, temp_hidden_names_list) == -1) {
            temp_hidden_names_list.push(column_name);
        }
    }

    var column_str = temp_hidden_names_list.toString();

    $.ajax({
        url: "{% url 'users:update_user_chart_preferences' %}",
        dataType: 'text',
        data: {
            'table_name': table_name,
            'column_list': column_str
        },
        type: 'POST',
        success: function () {
            // alert("Success");
        },
        error: function () {
            // alert("Error Updating Chart Preferences");
        }
    });

}

// the column names to hide are entered in the column preferences table
function hide_user_column_preferences_by_column_name(temp_table_id, prefix) {

    var hide_columns_json;

    var max_columns = 0;

    if (prefix === "qah") {

        hide_columns_json = home_qa_hide_columns_json;
        max_columns = home_qa_all_column_names_list.length;

    } else if (prefix === "qih") {

        hide_columns_json = home_qi_hide_columns_json;
        max_columns = home_qi_all_column_names_list.length;

    } else if (prefix === "reh") {

        hide_columns_json = home_re_hide_columns_json;
        max_columns = home_re_all_column_names_list.length;

    } else if (prefix === "teh") {

        hide_columns_json = home_te_hide_columns_json;
        max_columns = home_te_all_column_names_list.length;

    } else if (prefix === "tlh") {

        hide_columns_json = home_tl_hide_columns_json;
        max_columns = home_tl_all_column_names_list.length;

    }

    if (hide_columns_json === undefined) {
        // this will be undefined for the date_table if the user has not entered any column preferences for the table
    } else {

        if (hide_columns_json === '[]' || hide_columns_json === '' || hide_columns_json === "") {
            // alert("1604 empty json " + temp_table_id);
        } else {

            var temp_json_str = $.parseJSON(hide_columns_json);  // comma separated list of strings

            var temp_array = temp_json_str.split(",");

            if (Number(max_columns) == temp_array.length) {
                // hide the whole table
                // $('#' + temp_button).prop("disabled", true);

                // $('#td_' + temp_table_id).hide();

            } else {

                // create a list of column_numbers to hide then call the fnSetColumnVis
                var column_number_list = [];

                for (var index01 = 0; index01 < temp_array.length; index01++) {

                    var column_name = temp_array[index01].trim();
                    var column_number = get_column_number_by_name(temp_table_id, prefix, column_name);

                    // if the user has entered a column name that cannot be found in the table, the column_number will be -1
                    if (column_number > -1) {

                        if ($.inArray(column_number, column_number_list) == -1) {
                            column_number_list.push(column_number);
                        }

                    }
                }

                var oTable = $('#' + temp_table_id).dataTable();

                for (var index02 = 0; index02 < column_number_list.length; index02++) {

                    var hide_column_number = column_number_list[index02];
                    oTable.fnSetColumnVis(Number(hide_column_number), false, false);

                }
                oTable.fnDraw();
            }
        }
    }
}

function get_column_number_by_name(temp_table_id, prefix, column_name) {

    var column_number = -1;

    $('#' + temp_table_id).find('th').each(function ($index) {
        var temp_name = $(this).text().trim();

        if (temp_name === column_name) {
            column_number = $index;
        }
    });

    return column_number;
}

