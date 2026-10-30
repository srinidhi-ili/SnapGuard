import boto3
import os

from botocore.exceptions import (
    BotoCoreError,
    ClientError,
    NoCredentialsError
)


def get_aws_snapshots():
    """
    Retrieve EBS snapshots owned by the configured AWS account.

    Returns:
        dict: Snapshot data on success or error details on failure.
    """
    region = os.getenv("AWS_DEFAULT_REGION", "ap-south-1")

    try:
        ec2 = boto3.client("ec2", region_name=region)

        response = ec2.describe_snapshots(OwnerIds=["self"])

        snapshots = []

        for snapshot in response.get("Snapshots", []):
            snapshots.append({
                "snapshot_id": snapshot.get("SnapshotId"),
                "volume_id": snapshot.get("VolumeId"),
                "created_on": (
                    snapshot["StartTime"].isoformat()
                    if snapshot.get("StartTime")
                    else None
                ),
                "size_gb": snapshot.get("VolumeSize"),
                "status": snapshot.get("State"),
                "description": snapshot.get("Description", "")
            })

        return {
            "success": True,
            "region": region,
            "total_snapshots": len(snapshots),
            "snapshots": snapshots
        }

    except NoCredentialsError:
        error_message = (
            "AWS credentials were not found. "
            "Configure AWS authentication before retrying."
        )

    except ClientError as error:
        error_message = error.response.get(
            "Error", {}
        ).get("Message", "AWS service request failed.")

    except BotoCoreError as error:
        error_message = str(error)

    return {
        "success": False,
        "region": region,
        "error": error_message
    }
