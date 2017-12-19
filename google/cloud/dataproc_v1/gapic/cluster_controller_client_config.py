config = {
    "interfaces": {
        "google.cloud.dataproc.v1.ClusterController": {
            "retry_codes": {
                "idempotent": ["DEADLINE_EXCEEDED", "UNAVAILABLE"],
                "non_idempotent": []
            },
            "retry_params": {
                "default": {
                    "initial_retry_delay_millis": 100,
                    "retry_delay_multiplier": 1.3,
                    "max_retry_delay_millis": 60000,
                    "initial_rpc_timeout_millis": 10000,
                    "rpc_timeout_multiplier": 1.0,
                    "max_rpc_timeout_millis": 10000,
                    "total_timeout_millis": 300000
                }
            },
            "methods": {
                "CreateCluster": {
                    "timeout_millis": 90000,
                    "retry_codes_name": "non_idempotent",
                    "retry_params_name": "default"
                },
                "UpdateCluster": {
                    "timeout_millis": 30000,
                    "retry_codes_name": "non_idempotent",
                    "retry_params_name": "default"
                },
                "DeleteCluster": {
                    "timeout_millis": 15000,
                    "retry_codes_name": "idempotent",
                    "retry_params_name": "default"
                },
                "GetCluster": {
                    "timeout_millis": 10000,
                    "retry_codes_name": "idempotent",
                    "retry_params_name": "default"
                },
                "ListClusters": {
                    "timeout_millis": 10000,
                    "retry_codes_name": "idempotent",
                    "retry_params_name": "default"
                },
                "DiagnoseCluster": {
                    "timeout_millis": 10000,
                    "retry_codes_name": "non_idempotent",
                    "retry_params_name": "default"
                }
            }
        }
    }
}
