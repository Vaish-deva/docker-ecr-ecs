 if status_1 == 'stopped':
        # Start instance_1
        ec2.start_instances(InstanceIds=[instance_1])
        print(f'Starting instance {instance_1}')
        
        # Wait for 15 minutes before starting instance_2
        time.sleep(1 * 60)
        
        # Check the status of instance_2 again before starting it
        response_2 = ec2.describe_instance_status(InstanceIds=[instance_2])
        status_2 = response_2['InstanceStatuses'][0]['InstanceState']['Name'] if response_2['InstanceStatuses'] else 'stopped'
        
        if status_2 == 'stopped':
            ec2.start_instances(InstanceIds=[instance_2])
            print(f'Starting instance {instance_2}')
        else:
            print(f'Instance {instance_2} is already running')
    
    elif status_1 == 'running':
        # Check status of instance_2
        if status_2 == 'stopped':
            ec2.start_instances(InstanceIds=[instance_2])
            print(f'Starting instance {instance_2}')
        else:
            print(f'Instance {instance_2} is already running')

    return {
        'statusCode': 200,
        'body': 'Script executed successfully'
    }
