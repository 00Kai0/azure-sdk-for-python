# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.0.6282, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum

class AzureScaleType(str, Enum):
    """Scale type.
    """

    automatic = "automatic"
    manual = "manual"
    none = "none"

class AzureSkuName(str, Enum):
    """SKU name.
    """

    standard_ds13_v2_1_tb_ps = "Standard_DS13_v2+1TB_PS"
    standard_ds13_v2_2_tb_ps = "Standard_DS13_v2+2TB_PS"
    standard_ds14_v2_3_tb_ps = "Standard_DS14_v2+3TB_PS"
    standard_ds14_v2_4_tb_ps = "Standard_DS14_v2+4TB_PS"
    standard_d13_v2 = "Standard_D13_v2"
    standard_d14_v2 = "Standard_D14_v2"
    standard_l8_s = "Standard_L8s"
    standard_l16_s = "Standard_L16s"
    standard_d11_v2 = "Standard_D11_v2"
    standard_d12_v2 = "Standard_D12_v2"
    standard_l4_s = "Standard_L4s"
    dev_no_sla_standard_d11_v2 = "Dev(No SLA)_Standard_D11_v2"
    standard_e2_a_v4 = "Standard_E2a_v4"
    standard_e4_a_v4 = "Standard_E4a_v4"
    standard_e8_a_v4 = "Standard_E8a_v4"
    standard_e16_a_v4 = "Standard_E16a_v4"
    standard_e8_as_v4_1_tb_ps = "Standard_E8as_v4+1TB_PS"
    standard_e8_as_v4_2_tb_ps = "Standard_E8as_v4+2TB_PS"
    standard_e16_as_v4_3_tb_ps = "Standard_E16as_v4+3TB_PS"
    standard_e16_as_v4_4_tb_ps = "Standard_E16as_v4+4TB_PS"
    dev_no_sla_standard_e2_a_v4 = "Dev(No SLA)_Standard_E2a_v4"

class AzureSkuTier(str, Enum):
    """SKU tier.
    """

    basic = "Basic"
    standard = "Standard"

class ClusterPrincipalRole(str, Enum):
    """Cluster principal role.
    """

    all_databases_admin = "AllDatabasesAdmin"
    all_databases_viewer = "AllDatabasesViewer"

class Compression(str, Enum):
    """The compression type
    """

    none = "None"
    g_zip = "GZip"

class DatabasePrincipalRole(str, Enum):
    """Database principal role.
    """

    admin = "Admin"
    ingestor = "Ingestor"
    monitor = "Monitor"
    user = "User"
    unrestricted_viewers = "UnrestrictedViewers"
    viewer = "Viewer"

class DatabasePrincipalType(str, Enum):
    """Database principal type.
    """

    app = "App"
    group = "Group"
    user = "User"

class DefaultPrincipalsModificationKind(str, Enum):
    """The default principals modification kind
    """

    union = "Union"
    replace = "Replace"
    none = "None"

class EventGridDataFormat(str, Enum):
    """The data format of the message. Optionally the data format can be added to each message.
    """

    multijson = "MULTIJSON"
    json = "JSON"
    csv = "CSV"
    tsv = "TSV"
    scsv = "SCSV"
    sohsv = "SOHSV"
    psv = "PSV"
    txt = "TXT"
    raw = "RAW"
    singlejson = "SINGLEJSON"
    avro = "AVRO"
    tsve = "TSVE"
    parquet = "PARQUET"
    orc = "ORC"

class EventHubDataFormat(str, Enum):
    """The data format of the message. Optionally the data format can be added to each message.
    """

    multijson = "MULTIJSON"
    json = "JSON"
    csv = "CSV"
    tsv = "TSV"
    scsv = "SCSV"
    sohsv = "SOHSV"
    psv = "PSV"
    txt = "TXT"
    raw = "RAW"
    singlejson = "SINGLEJSON"
    avro = "AVRO"
    tsve = "TSVE"
    parquet = "PARQUET"
    orc = "ORC"

class IdentityType(str, Enum):
    """The identity type.
    """

    none = "None"
    system_assigned = "SystemAssigned"

class IotHubDataFormat(str, Enum):
    """The data format of the message. Optionally the data format can be added to each message.
    """

    multijson = "MULTIJSON"
    json = "JSON"
    csv = "CSV"
    tsv = "TSV"
    scsv = "SCSV"
    sohsv = "SOHSV"
    psv = "PSV"
    txt = "TXT"
    raw = "RAW"
    singlejson = "SINGLEJSON"
    avro = "AVRO"
    tsve = "TSVE"
    parquet = "PARQUET"
    orc = "ORC"

class Kind(str, Enum):
    """Kind of the database
    """

    read_write = "ReadWrite"
    read_only_following = "ReadOnlyFollowing"
    event_hub = "EventHub"
    event_grid = "EventGrid"
    iot_hub = "IotHub"

class LanguageExtensionName(str, Enum):
    """Language extension that can run within KQL query.
    """

    python = "PYTHON"
    r = "R"

class PrincipalsModificationKind(str, Enum):
    """The principals modification kind of the database
    """

    union = "Union"
    replace = "Replace"
    none = "None"

class PrincipalType(str, Enum):
    """Principal type.
    """

    app = "App"
    group = "Group"
    user = "User"

class ProvisioningState(str, Enum):
    """The provisioned state of the resource.
    """

    running = "Running"
    creating = "Creating"
    deleting = "Deleting"
    succeeded = "Succeeded"
    failed = "Failed"
    moving = "Moving"

class Reason(str, Enum):
    """Message providing the reason why the given name is invalid.
    """

    invalid = "Invalid"
    already_exists = "AlreadyExists"

class State(str, Enum):
    """The state of the resource.
    """

    creating = "Creating"
    unavailable = "Unavailable"
    running = "Running"
    deleting = "Deleting"
    deleted = "Deleted"
    stopping = "Stopping"
    stopped = "Stopped"
    starting = "Starting"
    updating = "Updating"

class Type(str, Enum):
    """The type of resource, Microsoft.Kusto/clusters.
    """

    microsoft_kusto_clusters = "Microsoft.Kusto/clusters"
    microsoft_kusto_clusters_databases = "Microsoft.Kusto/clusters/databases"
    microsoft_kusto_clusters_attached_database_configurations = "Microsoft.Kusto/clusters/attachedDatabaseConfigurations"
    microsoft_kusto_clusters_principal_assignments = "Microsoft.Kusto/clusters/principalAssignments"
    microsoft_kusto_clusters_databases_data_connections = "Microsoft.Kusto/clusters/databases/dataConnections"
    microsoft_kusto_clusters_databases_principal_assignments = "Microsoft.Kusto/clusters/databases/principalAssignments"
