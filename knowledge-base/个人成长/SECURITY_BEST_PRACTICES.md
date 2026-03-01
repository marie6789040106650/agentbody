# API Key Security Best Practices

## General Principles

1. **Never commit API keys to version control** - Use placeholders or environment variables
2. **Principle of least privilege** - Use API keys with minimal required permissions
3. **Regular rotation** - Change API keys periodically
4. **Access monitoring** - Monitor usage patterns for anomalies
5. **Secure transmission** - Always use HTTPS/TLS when transmitting keys

## Storage Security

### File Permissions
- Configuration files containing API keys should have restrictive permissions (600)
- Owner should be the minimal-privileged user that requires access
- Group and other permissions should be denied

### Environment Variables
- Often preferred method for containerized applications
- Not written to disk, stored in memory
- Still need to secure the mechanism that sets them

### Secrets Management Systems
- HashiCorp Vault
- AWS Secrets Manager
- Azure Key Vault
- Google Cloud Secret Manager
- Kubernetes secrets

## Transmission Security

1. **Always use HTTPS** - Never transmit API keys over unencrypted connections
2. **Avoid logging** - Ensure API keys are not logged in application logs
3. **Header usage** - Pass API keys in HTTP headers rather than URL parameters
4. **Short-lived tokens** - Where possible, use short-lived tokens instead of long-term keys

## Detection of Compromise

1. **Usage monitoring** - Track request volume and patterns
2. **Geographic monitoring** - Watch for requests from unexpected locations
3. **Resource access patterns** - Monitor what resources are being accessed
4. **Time-based patterns** - Look for access during unusual hours

## Incident Response

1. **Immediate revocation** - Revoke compromised keys immediately
2. **Audit trail** - Review all activity associated with the key
3. **Rotation** - Deploy new keys quickly
4. **Notification** - Notify relevant parties of compromise
5. **Analysis** - Determine root cause to prevent recurrence

## Code-Level Security

1. **Input validation** - Validate API keys meet expected format
2. **Output sanitization** - Ensure keys are never output in error messages
3. **Memory management** - Clear key values from memory when no longer needed
4. **Dependency security** - Keep libraries and frameworks updated

## Common Mistakes to Avoid

1. ✗ Hardcoding API keys in source code
2. ✗ Storing API keys in publicly accessible locations
3. ✗ Using the same API key across multiple applications
4. ✗ Transmitting API keys via URL parameters
5. ✗ Logging API keys in application logs
6. ✗ Failing to restrict file permissions on config files
7. ✗ Sharing API keys between development and production
8. ✗ Using default or weak API key passwords