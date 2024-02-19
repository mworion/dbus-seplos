import QtQuick 1.1
import com.victron.velib 1.0
import "utils.js" as Utils

MbPage {
    id: root
	property string bindPrefix

    title: service.description + " - Temperatures"
    model: VisibleItemModel {
        MbItemValue {
            description: qsTr("Battery Box temperature")
            show: item.valid
            item {
                bind: service.path("/Dc/0/Temperature")
                unit: "°C"
                decimals: 1
            }
        }
        MbItemValue {
            description: qsTr("MOSFET temperature")
            show: item.valid
            item {
                bind: service.path("/System/MOSFET_Temperature")
                unit: "°C"
                decimals: 1
            }
        }
		MbItemValue {
			description: qsTr("Cell temperature 1")
			item {
				bind: Utils.path(root.bindPrefix, "/System/Temperature1")
                unit: "°C"
                decimals: 1
			}
		}
		MbItemValue {
			description: qsTr("Cell temperature 2")
			item {
				bind: Utils.path(root.bindPrefix, "/System/Temperature2")
                unit: "°C"
                decimals: 1
			}
		}
		MbItemValue {
			description: qsTr("Cell temperature 3")
			item {
				bind: Utils.path(root.bindPrefix, "/System/Temperature3")
                unit: "°C"
                decimals: 1
			}
		}
		MbItemValue {
			description: qsTr("Cell temperature 4")
			item {
				bind: Utils.path(root.bindPrefix, "/System/Temperature4")
                unit: "°C"
                decimals: 1
			}
		}
    }
}