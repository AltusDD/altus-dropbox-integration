# Empire Command Center — Data Dictionary
_Generated: 2025-08-12T13:01:00.735088Z_

## Tables

### `accounts`
**Primary Key:** `id, id`
**Indexes:** 2

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `int4` | `NO` | `nextval('accounts_id_seq'::regclass)` |
| `doorloop_id` | `varchar` | `NO` | `` |
| `name` | `text` | `YES` | `` |
| `type` | `text` | `YES` | `` |
| `active` | `bool` | `YES` | `true` |
| `description` | `text` | `YES` | `` |
| `created_at` | `timestamptz` | `YES` | `` |
| `updated_at` | `timestamptz` | `YES` | `` |

### `audit_logs`
**Primary Key:** `id`
**Indexes:** 1

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `int8` | `NO` | `` |
| `batch_id` | `uuid` | `YES` | `` |
| `status` | `text` | `YES` | `` |
| `entity` | `text` | `YES` | `` |
| `entity_type` | `text` | `YES` | `` |
| `message` | `text` | `YES` | `` |
| `timestamp` | `timestamptz` | `YES` | `now()` |

### `case_history`
**Primary Key:** `id`
**Indexes:** 3

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `uuid` | `NO` | `gen_random_uuid()` |
| `legal_case_id` | `uuid` | `YES` | `` |
| `change_type` | `text` | `NO` | `` |
| `changed_by` | `text` | `YES` | `` |
| `change_details` | `jsonb` | `YES` | `` |
| `created_at` | `timestamptz` | `YES` | `now()` |

### `case_tags`
**Primary Key:** `id`
**Indexes:** 3

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `uuid` | `NO` | `gen_random_uuid()` |
| `legal_case_id` | `uuid` | `YES` | `` |
| `tag` | `text` | `NO` | `` |
| `created_at` | `timestamptz` | `YES` | `now()` |

### `collection_actions`
**Primary Key:** `id, id`
**Foreign Keys:** 1
**Indexes:** 1

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `int8` | `NO` | `` |
| `lease_id` | `int8` | `NO` | `` |
| `tenant_id` | `int8` | `YES` | `` |
| `status` | `text` | `YES` | `` |
| `stage` | `text` | `NO` | `` |
| `due_date` | `date` | `YES` | `` |
| `amount_due` | `numeric` | `YES` | `` |
| `notice_sent_at` | `timestamptz` | `YES` | `` |
| `notes` | `text` | `YES` | `` |
| `created_at` | `timestamptz` | `NO` | `timezone('utc'::text, now())` |
| `updated_at` | `timestamptz` | `NO` | `timezone('utc'::text, now())` |

### `communications`
**Primary Key:** `id, id`
**Indexes:** 2

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `int4` | `NO` | `nextval('communications_id_seq'::regclass)` |
| `doorloop_id` | `varchar` | `NO` | `` |
| `subject` | `text` | `YES` | `` |
| `body_preview` | `text` | `YES` | `` |
| `sent_at` | `timestamptz` | `YES` | `` |
| `type` | `text` | `YES` | `` |
| `status` | `text` | `YES` | `` |
| `thread_id` | `text` | `YES` | `` |
| `created_at` | `timestamptz` | `YES` | `` |
| `updated_at` | `timestamptz` | `YES` | `` |

### `damages_claims`
**Primary Key:** `id, id`
**Indexes:** 2

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `int8` | `NO` | `` |
| `case_number` | `text` | `YES` | `` |
| `lease_id` | `int8` | `YES` | `` |
| `property_id` | `int8` | `YES` | `` |
| `status` | `text` | `YES` | `` |
| `claim_amount` | `numeric` | `YES` | `` |
| `incident_date` | `date` | `YES` | `` |
| `filing_date` | `date` | `YES` | `` |
| `settlement_amount` | `numeric` | `YES` | `` |
| `notes` | `text` | `YES` | `` |
| `created_at` | `timestamptz` | `NO` | `timezone('utc'::text, now())` |
| `updated_at` | `timestamptz` | `NO` | `timezone('utc'::text, now())` |

### `doorloop_normalized_reports`

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `text` | `YES` | `` |
| `batch` | `text` | `YES` | `` |
| `data` | `jsonb` | `YES` | `` |
| `createdat` | `timestamptz` | `YES` | `` |
| `updatedat` | `timestamptz` | `YES` | `` |
| `_raw_payload` | `jsonb` | `YES` | `` |

### `doorloop_normalized_tasks`
**Primary Key:** `doorloop_id`
**Indexes:** 1

| Column | Type | Nullable | Default |
|---|---|---|---|
| `doorloop_id` | `text` | `NO` | `` |
| `property_id` | `text` | `YES` | `` |
| `vendor_id` | `text` | `YES` | `` |

### `doorloop_normalized_tenants`
**Primary Key:** `doorloop_id`
**Indexes:** 1

| Column | Type | Nullable | Default |
|---|---|---|---|
| `doorloop_id` | `text` | `NO` | `` |
| `name` | `text` | `YES` | `` |

### `doorloop_normalized_units`
**Primary Key:** `doorloop_id`
**Indexes:** 1

| Column | Type | Nullable | Default |
|---|---|---|---|
| `doorloop_id` | `text` | `NO` | `` |
| `name` | `text` | `YES` | `` |
| `property_id` | `text` | `YES` | `` |

### `doorloop_normalized_users`

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `text` | `YES` | `` |
| `data` | `jsonb` | `YES` | `` |
| `source_endpoint` | `text` | `YES` | `` |
| `inserted_at` | `timestamptz` | `YES` | `` |
| `companyName` | `text` | `YES` | `` |
| `firstName` | `text` | `YES` | `` |
| `createdBy` | `text` | `YES` | `` |
| `active` | `bool` | `YES` | `` |
| `createdAt` | `timestamptz` | `YES` | `` |
| `emails` | `jsonb` | `YES` | `` |
| `invitationLastSentAt` | `timestamptz` | `YES` | `` |
| `jobTitle` | `text` | `YES` | `` |
| `fullName` | `text` | `YES` | `` |
| `updatedAt` | `timestamptz` | `YES` | `` |
| `primaryAddress` | `jsonb` | `YES` | `` |
| `lastSeenAt` | `timestamptz` | `YES` | `` |
| `bankAccounts` | `jsonb` | `YES` | `` |
| `propertyGroups` | `jsonb` | `YES` | `` |
| `properties` | `jsonb` | `YES` | `` |
| `e164PhoneMobileNumber` | `text` | `YES` | `` |
| `phones` | `jsonb` | `YES` | `` |
| `role` | `text` | `YES` | `` |
| `intercomContactId` | `text` | `YES` | `` |
| `timezone` | `text` | `YES` | `` |
| `loginEmail` | `text` | `YES` | `` |
| `name` | `text` | `YES` | `` |
| `updatedBy` | `text` | `YES` | `` |
| `lastName` | `text` | `YES` | `` |
| `status` | `text` | `YES` | `` |
| `owner` | `bool` | `YES` | `` |
| `pictureUrl` | `text` | `YES` | `` |
| `batch` | `text` | `YES` | `` |
| `doorloop_id` | `text` | `YES` | `` |

### `doorloop_normalized_vendor_bills`

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `text` | `YES` | `` |
| `data` | `jsonb` | `YES` | `` |
| `source_endpoint` | `text` | `YES` | `` |
| `inserted_at` | `timestamptz` | `YES` | `` |
| `totalAmount` | `int8` | `YES` | `` |
| `lines` | `jsonb` | `YES` | `` |
| `vendor` | `text` | `YES` | `` |
| `workOrder` | `text` | `YES` | `` |
| `totalBalance` | `numeric` | `YES` | `` |
| `batch` | `text` | `YES` | `` |
| `updatedAt` | `timestamptz` | `YES` | `` |
| `dueDate` | `timestamptz` | `YES` | `` |
| `memo` | `text` | `YES` | `` |
| `createdBy` | `text` | `YES` | `` |
| `createdAt` | `timestamptz` | `YES` | `` |
| `date` | `timestamptz` | `YES` | `` |
| `recurringTransaction` | `text` | `YES` | `` |
| `register` | `jsonb` | `YES` | `` |
| `reference` | `text` | `YES` | `` |
| `updatedBy` | `text` | `YES` | `` |
| `amount` | `numeric` | `YES` | `` |

### `doorloop_normalized_vendor_credits`

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `text` | `YES` | `` |

### `doorloop_normalized_vendors`
**Primary Key:** `doorloop_id`
**Indexes:** 1

| Column | Type | Nullable | Default |
|---|---|---|---|
| `doorloop_id` | `text` | `NO` | `` |
| `name` | `text` | `YES` | `` |
| `balance` | `numeric` | `YES` | `` |

### `doorloop_pipeline_audit`
**Primary Key:** `id`
**Indexes:** 1

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `uuid` | `NO` | `gen_random_uuid()` |
| `batch_id` | `uuid` | `NO` | `` |
| `status` | `text` | `NO` | `` |
| `entity` | `text` | `NO` | `` |
| `message` | `text` | `YES` | `` |
| `timestamp` | `timestamptz` | `YES` | `now()` |
| `entity_type` | `text` | `NO` | `'sync'::text` |
| `request_url` | `text` | `YES` | `` |
| `record_count` | `int4` | `YES` | `` |
| `error` | `jsonb` | `YES` | `` |
| `extra` | `jsonb` | `YES` | `` |
| `created_at` | `timestamptz` | `YES` | `now()` |
| `updated_at` | `timestamptz` | `YES` | `now()` |

### `doorloop_raw_accounts`
**Primary Key:** `id`
**Indexes:** 1

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `text` | `NO` | `` |
| `data` | `jsonb` | `YES` | `` |
| `source_endpoint` | `text` | `YES` | `` |
| `inserted_at` | `timestamptz` | `YES` | `now()` |
| `leaseChargeItem` | `bool` | `YES` | `` |
| `active` | `bool` | `YES` | `` |
| `createdBy` | `text` | `YES` | `` |
| `outgoingEPayEnabled` | `bool` | `YES` | `` |
| `createdAt` | `timestamptz` | `YES` | `` |
| `type` | `text` | `YES` | `` |
| `updatedAt` | `timestamptz` | `YES` | `` |
| `parentAccount` | `text` | `YES` | `` |
| `systemAccount` | `bool` | `YES` | `` |
| `openingBalanceEntry` | `text` | `YES` | `` |
| `class` | `text` | `YES` | `` |
| `name` | `text` | `YES` | `` |
| `updatedBy` | `text` | `YES` | `` |
| `leaseDepositItem` | `bool` | `YES` | `` |
| `fullyQualifiedName` | `text` | `YES` | `` |
| `cashFlowActivity` | `text` | `YES` | `` |
| `taxable` | `bool` | `YES` | `` |
| `description` | `text` | `YES` | `` |
| `defaultAccountFor` | `jsonb` | `YES` | `` |
| `batch` | `text` | `YES` | `` |

### `doorloop_raw_activity_logs`
**Primary Key:** `id`
**Indexes:** 1

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `text` | `NO` | `` |
| `batch` | `text` | `YES` | `` |
| `data` | `jsonb` | `YES` | `` |
| `createdat` | `timestamptz` | `YES` | `` |
| `updatedat` | `timestamptz` | `YES` | `` |
| `_raw_payload` | `jsonb` | `YES` | `` |

### `doorloop_raw_applications`
**Primary Key:** `id`
**Indexes:** 1

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `text` | `NO` | `` |
| `batch` | `text` | `YES` | `` |
| `data` | `jsonb` | `YES` | `` |
| `createdat` | `timestamptz` | `YES` | `` |
| `updatedat` | `timestamptz` | `YES` | `` |
| `_raw_payload` | `jsonb` | `YES` | `` |

### `doorloop_raw_communications`
**Primary Key:** `id`
**Indexes:** 1

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `text` | `NO` | `` |
| `data` | `jsonb` | `YES` | `` |
| `source_endpoint` | `text` | `YES` | `` |
| `inserted_at` | `timestamptz` | `YES` | `now()` |
| `externalId` | `text` | `YES` | `` |
| `conversationMessage` | `text` | `YES` | `` |
| `subjectType` | `text` | `YES` | `` |
| `intercomReceiptId` | `text` | `YES` | `` |
| `createdBy` | `text` | `YES` | `` |
| `createdAt` | `timestamptz` | `YES` | `` |
| `cc` | `jsonb` | `YES` | `` |
| `bodyPreview` | `text` | `YES` | `` |
| `to` | `jsonb` | `YES` | `` |
| `announcement` | `text` | `YES` | `` |
| `type` | `text` | `YES` | `` |
| `updatedAt` | `timestamptz` | `YES` | `` |
| `openedAt` | `jsonb` | `YES` | `` |
| `sentAt` | `timestamptz` | `YES` | `` |
| `bouncedAt` | `timestamptz` | `YES` | `` |
| `conversation` | `text` | `YES` | `` |
| `failedReason` | `text` | `YES` | `` |
| `bcc` | `jsonb` | `YES` | `` |
| `subject` | `text` | `YES` | `` |
| `intercomContactId` | `text` | `YES` | `` |
| `from` | `jsonb` | `YES` | `` |
| `updatedBy` | `text` | `YES` | `` |
| `clickedAt` | `jsonb` | `YES` | `` |
| `intercomTemplateId` | `int8` | `YES` | `` |
| `status` | `text` | `YES` | `` |
| `batch` | `text` | `YES` | `` |

### `doorloop_raw_expenses`
**Primary Key:** `id`
**Indexes:** 1

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `text` | `NO` | `` |
| `data` | `jsonb` | `YES` | `` |
| `source_endpoint` | `text` | `YES` | `` |
| `inserted_at` | `timestamptz` | `YES` | `now()` |
| `isVoidedCheck` | `bool` | `YES` | `` |
| `paymentMethod` | `text` | `YES` | `` |
| `memo` | `text` | `YES` | `` |
| `createdBy` | `text` | `YES` | `` |
| `createdAt` | `timestamptz` | `YES` | `` |
| `ePayInfo` | `jsonb` | `YES` | `` |
| `register` | `jsonb` | `YES` | `` |
| `reference` | `text` | `YES` | `` |
| `batch` | `text` | `YES` | `` |
| `updatedAt` | `timestamptz` | `YES` | `` |
| `payToResourceId` | `text` | `YES` | `` |
| `totalAmount` | `numeric` | `YES` | `` |
| `checkInfo` | `jsonb` | `YES` | `` |
| `payToResourceType` | `text` | `YES` | `` |
| `date` | `timestamptz` | `YES` | `` |
| `payFromAccount` | `text` | `YES` | `` |
| `totalBalance` | `int8` | `YES` | `` |
| `updatedBy` | `text` | `YES` | `` |
| `lines` | `jsonb` | `YES` | `` |

### `doorloop_raw_files`
**Primary Key:** `id`
**Indexes:** 1

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `text` | `NO` | `` |
| `data` | `jsonb` | `YES` | `` |
| `source_endpoint` | `text` | `YES` | `` |
| `inserted_at` | `timestamptz` | `YES` | `now()` |
| `rank` | `int8` | `YES` | `` |
| `createdByType` | `text` | `YES` | `` |
| `notes` | `text` | `YES` | `` |
| `updatedAt` | `timestamptz` | `YES` | `` |
| `tags` | `jsonb` | `YES` | `` |
| `metadata` | `jsonb` | `YES` | `` |
| `unit` | `text` | `YES` | `` |
| `mimeType` | `text` | `YES` | `` |
| `createdBy` | `text` | `YES` | `` |
| `isSharedWithTenant` | `bool` | `YES` | `` |
| `createdByName` | `text` | `YES` | `` |
| `downloadUrl` | `text` | `YES` | `` |
| `size` | `int8` | `YES` | `` |
| `createdAt` | `timestamptz` | `YES` | `` |
| `name` | `text` | `YES` | `` |
| `linkedResource` | `jsonb` | `YES` | `` |
| `property` | `text` | `YES` | `` |
| `updatedBy` | `text` | `YES` | `` |
| `batch` | `text` | `YES` | `` |

### `doorloop_raw_inspections`
**Primary Key:** `id`
**Indexes:** 1

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `text` | `NO` | `` |
| `batch` | `text` | `YES` | `` |
| `data` | `jsonb` | `YES` | `` |
| `createdat` | `timestamptz` | `YES` | `` |
| `updatedat` | `timestamptz` | `YES` | `` |
| `_raw_payload` | `jsonb` | `YES` | `` |

### `doorloop_raw_insurance_policies`
**Primary Key:** `id`
**Indexes:** 1

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `text` | `NO` | `` |
| `batch` | `text` | `YES` | `` |
| `data` | `jsonb` | `YES` | `` |
| `createdat` | `timestamptz` | `YES` | `` |
| `updatedat` | `timestamptz` | `YES` | `` |
| `_raw_payload` | `jsonb` | `YES` | `` |

### `doorloop_raw_lease_charges`
**Primary Key:** `id`
**Indexes:** 1

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `text` | `NO` | `` |
| `data` | `jsonb` | `YES` | `` |
| `source_endpoint` | `text` | `YES` | `` |
| `inserted_at` | `timestamptz` | `YES` | `now()` |
| `memo` | `text` | `YES` | `` |
| `createdBy` | `text` | `YES` | `` |
| `createdAt` | `timestamptz` | `YES` | `` |
| `register` | `jsonb` | `YES` | `` |
| `reference` | `text` | `YES` | `` |
| `lateFeeForLeaseCharge` | `text` | `YES` | `` |
| `batch` | `text` | `YES` | `` |
| `updatedAt` | `timestamptz` | `YES` | `` |
| `totalAmount` | `numeric` | `YES` | `` |
| `isFilesSharedWithTenant` | `bool` | `YES` | `` |
| `date` | `timestamptz` | `YES` | `` |
| `totalBalance` | `numeric` | `YES` | `` |
| `lastLateFeesProcessedDate` | `timestamptz` | `YES` | `` |
| `recurringTransaction` | `text` | `YES` | `` |
| `updatedBy` | `text` | `YES` | `` |
| `lines` | `jsonb` | `YES` | `` |
| `lease` | `text` | `YES` | `` |

### `doorloop_raw_lease_credits`
**Primary Key:** `id`
**Indexes:** 1

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `text` | `NO` | `` |
| `data` | `jsonb` | `YES` | `` |
| `source_endpoint` | `text` | `YES` | `` |
| `inserted_at` | `timestamptz` | `YES` | `now()` |
| `totalAmount` | `int8` | `YES` | `` |
| `lines` | `jsonb` | `YES` | `` |
| `batch` | `text` | `YES` | `` |
| `updatedAt` | `timestamptz` | `YES` | `` |
| `createdBy` | `text` | `YES` | `` |
| `totalBalance` | `int8` | `YES` | `` |
| `lease` | `text` | `YES` | `` |
| `isFilesSharedWithTenant` | `bool` | `YES` | `` |
| `createdAt` | `timestamptz` | `YES` | `` |
| `date` | `timestamptz` | `YES` | `` |
| `register` | `jsonb` | `YES` | `` |
| `reference` | `text` | `YES` | `` |
| `updatedBy` | `text` | `YES` | `` |
| `amount` | `numeric` | `YES` | `` |

### `doorloop_raw_lease_payments`
**Primary Key:** `id`
**Indexes:** 1

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `text` | `NO` | `` |
| `data` | `jsonb` | `YES` | `` |
| `source_endpoint` | `text` | `YES` | `` |
| `inserted_at` | `timestamptz` | `YES` | `now()` |
| `depositEntry` | `text` | `YES` | `` |
| `amountNotAppliedToCharges` | `numeric` | `YES` | `` |
| `paymentMethod` | `text` | `YES` | `` |
| `autoApplyPaymentOnCharges` | `bool` | `YES` | `` |
| `reversedPaymentMemo` | `text` | `YES` | `` |
| `memo` | `text` | `YES` | `` |
| `createdBy` | `text` | `YES` | `` |
| `ePayInfo` | `jsonb` | `YES` | `` |
| `createdAt` | `timestamptz` | `YES` | `` |
| `receivedFromTenant` | `text` | `YES` | `` |
| `register` | `jsonb` | `YES` | `` |
| `reference` | `text` | `YES` | `` |
| `updatedAt` | `timestamptz` | `YES` | `` |
| `linkedCharges` | `jsonb` | `YES` | `` |
| `linkedCredits` | `jsonb` | `YES` | `` |
| `checkInfo` | `jsonb` | `YES` | `` |
| `isFilesSharedWithTenant` | `bool` | `YES` | `` |
| `date` | `timestamptz` | `YES` | `` |
| `depositToAccount` | `text` | `YES` | `` |
| `reversedPayment` | `text` | `YES` | `` |
| `amountAppliedToCredits` | `numeric` | `YES` | `` |
| `amountReceived` | `numeric` | `YES` | `` |
| `recurringTransaction` | `text` | `YES` | `` |
| `updatedBy` | `text` | `YES` | `` |
| `amountAppliedToCharges` | `numeric` | `YES` | `` |
| `depositStatus` | `text` | `YES` | `` |
| `lease` | `text` | `YES` | `` |
| `reversedPaymentDate` | `timestamptz` | `YES` | `` |
| `batch` | `text` | `YES` | `` |

### `doorloop_raw_lease_reversed_payments`
**Primary Key:** `id`
**Indexes:** 1

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `text` | `NO` | `` |
| `data` | `jsonb` | `YES` | `` |
| `source_endpoint` | `text` | `YES` | `` |
| `inserted_at` | `timestamptz` | `YES` | `now()` |
| `updatedAt` | `timestamptz` | `YES` | `` |
| `depositStatus` | `text` | `YES` | `` |
| `processorFee` | `int8` | `YES` | `` |
| `memo` | `text` | `YES` | `` |
| `lease` | `text` | `YES` | `` |
| `createdAt` | `timestamptz` | `YES` | `` |
| `date` | `timestamptz` | `YES` | `` |
| `leasePayment` | `text` | `YES` | `` |
| `register` | `jsonb` | `YES` | `` |
| `reference` | `text` | `YES` | `` |
| `reason` | `text` | `YES` | `` |
| `batch` | `text` | `YES` | `` |

### `doorloop_raw_leases`
**Primary Key:** `id`
**Indexes:** 1

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `text` | `NO` | `` |
| `data` | `jsonb` | `YES` | `` |
| `source_endpoint` | `text` | `YES` | `` |
| `inserted_at` | `timestamptz` | `YES` | `now()` |
| `currentBalance` | `int8` | `YES` | `` |
| `proofOfInsuranceProvided` | `bool` | `YES` | `` |
| `evictionPending` | `bool` | `YES` | `` |
| `createdBy` | `text` | `YES` | `` |
| `totalRecurringRent` | `numeric` | `YES` | `` |
| `createdAt` | `timestamptz` | `YES` | `` |
| `totalRecurringCharges` | `int8` | `YES` | `` |
| `recurringRentStatus` | `text` | `YES` | `` |
| `totalRecurringCredits` | `int8` | `YES` | `` |
| `proofOfInsuranceProvidedAt` | `timestamptz` | `YES` | `` |
| `reference` | `text` | `YES` | `` |
| `batch` | `text` | `YES` | `` |
| `notes` | `text` | `YES` | `` |
| `updatedAt` | `timestamptz` | `YES` | `` |
| `start` | `timestamptz` | `YES` | `` |
| `end` | `timestamptz` | `YES` | `` |
| `totalDepositsHeld` | `numeric` | `YES` | `` |
| `proofOfInsuranceExpirationDate` | `timestamptz` | `YES` | `` |
| `lastLateFeesProcessedDate` | `timestamptz` | `YES` | `` |
| `renewalInfo` | `jsonb` | `YES` | `` |
| `settings` | `jsonb` | `YES` | `` |
| `outstandingBalance` | `numeric` | `YES` | `` |
| `name` | `text` | `YES` | `` |
| `totalBalanceDue` | `numeric` | `YES` | `` |
| `property` | `text` | `YES` | `` |
| `updatedBy` | `text` | `YES` | `` |
| `term` | `text` | `YES` | `` |
| `totalRecurringPayments` | `numeric` | `YES` | `` |
| `rolloverToAtWill` | `bool` | `YES` | `` |
| `proofOfInsuranceRequired` | `bool` | `YES` | `` |
| `recurringRentFrequency` | `text` | `YES` | `` |
| `overdueBalance` | `numeric` | `YES` | `` |
| `proofOfInsuranceStatus` | `text` | `YES` | `` |
| `upcomingBalance` | `int8` | `YES` | `` |
| `status` | `text` | `YES` | `` |
| `proofOfInsuranceEffectiveDate` | `timestamptz` | `YES` | `` |
| `units` | `jsonb` | `YES` | `` |

### `doorloop_raw_notes`
**Primary Key:** `id`
**Indexes:** 1

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `text` | `NO` | `` |
| `data` | `jsonb` | `YES` | `` |
| `source_endpoint` | `text` | `YES` | `` |
| `inserted_at` | `timestamptz` | `YES` | `now()` |
| `title` | `text` | `YES` | `` |
| `body` | `text` | `YES` | `` |
| `updatedAt` | `timestamptz` | `YES` | `` |
| `tags` | `jsonb` | `YES` | `` |
| `unit` | `text` | `YES` | `` |
| `createdBy` | `text` | `YES` | `` |
| `createdAt` | `timestamptz` | `YES` | `` |
| `linkedResource` | `jsonb` | `YES` | `` |
| `property` | `text` | `YES` | `` |
| `updatedBy` | `text` | `YES` | `` |
| `batch` | `text` | `YES` | `` |

### `doorloop_raw_owners`
**Primary Key:** `id`
**Indexes:** 1

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `text` | `NO` | `` |
| `data` | `jsonb` | `YES` | `` |
| `source_endpoint` | `text` | `YES` | `` |
| `inserted_at` | `timestamptz` | `YES` | `now()` |
| `outgoingEPay` | `jsonb` | `YES` | `` |
| `companyName` | `text` | `YES` | `` |
| `firstName` | `text` | `YES` | `` |
| `managementStartDate` | `timestamptz` | `YES` | `` |
| `active` | `bool` | `YES` | `` |
| `createdBy` | `text` | `YES` | `` |
| `createdAt` | `timestamptz` | `YES` | `` |
| `emails` | `jsonb` | `YES` | `` |
| `batch` | `text` | `YES` | `` |
| `fullName` | `text` | `YES` | `` |
| `jobTitle` | `text` | `YES` | `` |
| `updatedAt` | `timestamptz` | `YES` | `` |
| `primaryAddress` | `jsonb` | `YES` | `` |
| `properties` | `jsonb` | `YES` | `` |
| `e164PhoneMobileNumber` | `text` | `YES` | `` |
| `phones` | `jsonb` | `YES` | `` |
| `company` | `bool` | `YES` | `` |
| `alternateAddress` | `jsonb` | `YES` | `` |
| `intercomContactId` | `text` | `YES` | `` |
| `name` | `text` | `YES` | `` |
| `updatedBy` | `text` | `YES` | `` |
| `portalInfo` | `jsonb` | `YES` | `` |
| `conversationWelcomeSmsSentAt` | `timestamptz` | `YES` | `` |
| `lastName` | `text` | `YES` | `` |
| `notes` | `text` | `YES` | `` |

### `doorloop_raw_payments`
**Primary Key:** `id`
**Indexes:** 1

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `int8` | `NO` | `` |
| `created_at` | `timestamptz` | `YES` | `now()` |
| `data` | `jsonb` | `YES` | `` |

### `doorloop_raw_portfolios`
**Primary Key:** `id`
**Indexes:** 1

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `text` | `NO` | `` |
| `data` | `jsonb` | `YES` | `` |
| `source_endpoint` | `text` | `YES` | `` |
| `inserted_at` | `timestamptz` | `YES` | `now()` |
| `updatedAt` | `timestamptz` | `YES` | `` |
| `createdBy` | `text` | `YES` | `` |
| `properties` | `jsonb` | `YES` | `` |
| `createdAt` | `timestamptz` | `YES` | `` |
| `name` | `text` | `YES` | `` |
| `updatedBy` | `text` | `YES` | `` |
| `batch` | `text` | `YES` | `` |

### `doorloop_raw_properties`
**Primary Key:** `id`
**Indexes:** 1

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `text` | `NO` | `` |
| `data` | `jsonb` | `YES` | `` |
| `source_endpoint` | `text` | `YES` | `` |
| `inserted_at` | `timestamptz` | `YES` | `now()` |
| `active` | `bool` | `YES` | `` |
| `createdBy` | `text` | `YES` | `` |
| `boardMembers` | `jsonb` | `YES` | `` |
| `createdAt` | `timestamptz` | `YES` | `` |
| `amenities` | `jsonb` | `YES` | `` |
| `petsPolicy` | `jsonb` | `YES` | `` |
| `address` | `jsonb` | `YES` | `` |
| `batch` | `text` | `YES` | `` |
| `type` | `text` | `YES` | `` |
| `updatedAt` | `timestamptz` | `YES` | `` |
| `owners` | `jsonb` | `YES` | `` |
| `settings` | `jsonb` | `YES` | `` |
| `numActiveUnits` | `int8` | `YES` | `` |
| `class` | `text` | `YES` | `` |
| `name` | `text` | `YES` | `` |
| `updatedBy` | `text` | `YES` | `` |
| `pictures` | `jsonb` | `YES` | `` |
| `description` | `text` | `YES` | `` |
| `typeDescription` | `text` | `YES` | `` |

### `doorloop_raw_property_groups`
**Primary Key:** `id`
**Indexes:** 1

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `text` | `NO` | `` |
| `data` | `jsonb` | `YES` | `` |
| `source_endpoint` | `text` | `YES` | `` |

### `doorloop_raw_recurring_charges`
**Primary Key:** `id`
**Indexes:** 1

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `text` | `NO` | `` |
| `batch` | `text` | `YES` | `` |
| `data` | `jsonb` | `YES` | `` |
| `createdat` | `timestamptz` | `YES` | `` |
| `updatedat` | `timestamptz` | `YES` | `` |
| `_raw_payload` | `jsonb` | `YES` | `` |

### `doorloop_raw_recurring_credits`
**Primary Key:** `id`
**Indexes:** 1

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `text` | `NO` | `` |
| `batch` | `text` | `YES` | `` |
| `data` | `jsonb` | `YES` | `` |
| `createdat` | `timestamptz` | `YES` | `` |
| `updatedat` | `timestamptz` | `YES` | `` |
| `_raw_payload` | `jsonb` | `YES` | `` |

### `doorloop_raw_reports`
**Primary Key:** `id`
**Indexes:** 1

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `text` | `NO` | `` |
| `batch` | `text` | `YES` | `` |
| `data` | `jsonb` | `YES` | `` |
| `createdat` | `timestamptz` | `YES` | `` |
| `updatedat` | `timestamptz` | `YES` | `` |
| `_raw_payload` | `jsonb` | `YES` | `` |

### `doorloop_raw_tasks`
**Primary Key:** `id`
**Indexes:** 1

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `text` | `NO` | `` |
| `data` | `jsonb` | `YES` | `` |
| `source_endpoint` | `text` | `YES` | `` |
| `inserted_at` | `timestamptz` | `YES` | `now()` |
| `createdBy` | `text` | `YES` | `` |
| `createdAt` | `timestamptz` | `YES` | `` |
| `entryNotes` | `text` | `YES` | `` |
| `reference` | `text` | `YES` | `` |
| `assignedToUsers` | `jsonb` | `YES` | `` |
| `type` | `text` | `YES` | `` |
| `updatedAt` | `timestamptz` | `YES` | `` |
| `completedAt` | `timestamptz` | `YES` | `` |
| `entryPermission` | `text` | `YES` | `` |
| `createdByType` | `text` | `YES` | `` |
| `workOrder` | `jsonb` | `YES` | `` |
| `unit` | `text` | `YES` | `` |
| `dueDate` | `timestamptz` | `YES` | `` |
| `subject` | `text` | `YES` | `` |
| `recurringTransaction` | `text` | `YES` | `` |
| `property` | `text` | `YES` | `` |
| `updatedBy` | `text` | `YES` | `` |
| `dateType` | `text` | `YES` | `` |
| `requestedByTenant` | `text` | `YES` | `` |
| `requestedByUser` | `text` | `YES` | `` |
| `tenantRequestMaintenanceCategory` | `text` | `YES` | `` |
| `tenantRequestType` | `text` | `YES` | `` |
| `status` | `text` | `YES` | `` |
| `description` | `text` | `YES` | `` |
| `priority` | `text` | `YES` | `` |
| `linkedResource` | `jsonb` | `YES` | `` |
| `requestedByOwner` | `text` | `YES` | `` |
| `batch` | `text` | `YES` | `` |

### `doorloop_raw_tenants`
**Primary Key:** `id`
**Indexes:** 1

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `text` | `NO` | `` |
| `data` | `jsonb` | `YES` | `` |
| `source_endpoint` | `text` | `YES` | `` |
| `inserted_at` | `timestamptz` | `YES` | `now()` |
| `dateOfBirth` | `timestamptz` | `YES` | `` |
| `companyName` | `text` | `YES` | `` |
| `firstName` | `text` | `YES` | `` |
| `createdBy` | `text` | `YES` | `` |
| `createdAt` | `timestamptz` | `YES` | `` |
| `emails` | `jsonb` | `YES` | `` |
| `batch` | `text` | `YES` | `` |
| `fullName` | `text` | `YES` | `` |
| `type` | `text` | `YES` | `` |
| `updatedAt` | `timestamptz` | `YES` | `` |
| `notes` | `text` | `YES` | `` |
| `dependants` | `jsonb` | `YES` | `` |
| `primaryAddress` | `jsonb` | `YES` | `` |
| `e164PhoneMobileNumber` | `text` | `YES` | `` |
| `emergencyContacts` | `jsonb` | `YES` | `` |
| `phones` | `jsonb` | `YES` | `` |
| `company` | `bool` | `YES` | `` |
| `vehicles` | `jsonb` | `YES` | `` |
| `gender` | `text` | `YES` | `` |
| `acceptedOnTOS` | `timestamptz` | `YES` | `` |
| `intercomContactId` | `text` | `YES` | `` |
| `name` | `text` | `YES` | `` |
| `updatedBy` | `text` | `YES` | `` |
| `portalInfo` | `jsonb` | `YES` | `` |
| `middleName` | `text` | `YES` | `` |
| `otherScreeningService` | `text` | `YES` | `` |
| `stripeCustomerId` | `text` | `YES` | `` |
| `conversationWelcomeSmsSentAt` | `timestamptz` | `YES` | `` |
| `screeningService` | `text` | `YES` | `` |
| `lastName` | `text` | `YES` | `` |
| `prospectInfo` | `jsonb` | `YES` | `` |
| `pets` | `jsonb` | `YES` | `` |

### `doorloop_raw_units`
**Primary Key:** `id`
**Indexes:** 1

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `text` | `NO` | `` |
| `data` | `jsonb` | `YES` | `` |
| `source_endpoint` | `text` | `YES` | `` |
| `inserted_at` | `timestamptz` | `YES` | `now()` |
| `active` | `bool` | `YES` | `` |
| `createdBy` | `text` | `YES` | `` |
| `inEviction` | `bool` | `YES` | `` |
| `createdAt` | `timestamptz` | `YES` | `` |
| `amenities` | `jsonb` | `YES` | `` |
| `baths` | `numeric` | `YES` | `` |
| `address` | `jsonb` | `YES` | `` |
| `batch` | `text` | `YES` | `` |
| `addressSameAsProperty` | `bool` | `YES` | `` |
| `updatedAt` | `timestamptz` | `YES` | `` |
| `listed` | `bool` | `YES` | `` |
| `name` | `text` | `YES` | `` |
| `property` | `text` | `YES` | `` |
| `updatedBy` | `text` | `YES` | `` |
| `rentalApplicationListing` | `jsonb` | `YES` | `` |
| `pictures` | `jsonb` | `YES` | `` |
| `listing` | `jsonb` | `YES` | `` |
| `size` | `int8` | `YES` | `` |
| `description` | `text` | `YES` | `` |
| `beds` | `int8` | `YES` | `` |
| `marketRent` | `int8` | `YES` | `` |

### `doorloop_raw_users`
**Primary Key:** `id`
**Indexes:** 1

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `text` | `NO` | `` |
| `data` | `jsonb` | `YES` | `` |
| `source_endpoint` | `text` | `YES` | `` |
| `inserted_at` | `timestamptz` | `YES` | `now()` |
| `companyName` | `text` | `YES` | `` |
| `firstName` | `text` | `YES` | `` |
| `createdBy` | `text` | `YES` | `` |
| `active` | `bool` | `YES` | `` |
| `createdAt` | `timestamptz` | `YES` | `` |
| `emails` | `jsonb` | `YES` | `` |
| `invitationLastSentAt` | `timestamptz` | `YES` | `` |
| `jobTitle` | `text` | `YES` | `` |
| `fullName` | `text` | `YES` | `` |
| `updatedAt` | `timestamptz` | `YES` | `` |
| `primaryAddress` | `jsonb` | `YES` | `` |
| `lastSeenAt` | `timestamptz` | `YES` | `` |
| `bankAccounts` | `jsonb` | `YES` | `` |
| `propertyGroups` | `jsonb` | `YES` | `` |
| `properties` | `jsonb` | `YES` | `` |
| `e164PhoneMobileNumber` | `text` | `YES` | `` |
| `phones` | `jsonb` | `YES` | `` |
| `role` | `text` | `YES` | `` |
| `intercomContactId` | `text` | `YES` | `` |
| `timezone` | `text` | `YES` | `` |
| `loginEmail` | `text` | `YES` | `` |
| `name` | `text` | `YES` | `` |
| `updatedBy` | `text` | `YES` | `` |
| `lastName` | `text` | `YES` | `` |
| `status` | `text` | `YES` | `` |
| `owner` | `bool` | `YES` | `` |
| `pictureUrl` | `text` | `YES` | `` |
| `batch` | `text` | `YES` | `` |

### `doorloop_raw_vendor_bills`
**Primary Key:** `id`
**Indexes:** 1

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `text` | `NO` | `` |
| `data` | `jsonb` | `YES` | `` |
| `source_endpoint` | `text` | `YES` | `` |
| `inserted_at` | `timestamptz` | `YES` | `now()` |
| `totalAmount` | `int8` | `YES` | `` |
| `lines` | `jsonb` | `YES` | `` |
| `vendor` | `text` | `YES` | `` |
| `workOrder` | `text` | `YES` | `` |
| `totalBalance` | `numeric` | `YES` | `` |
| `batch` | `text` | `YES` | `` |
| `updatedAt` | `timestamptz` | `YES` | `` |
| `dueDate` | `timestamptz` | `YES` | `` |
| `memo` | `text` | `YES` | `` |
| `createdBy` | `text` | `YES` | `` |
| `createdAt` | `timestamptz` | `YES` | `` |
| `date` | `timestamptz` | `YES` | `` |
| `recurringTransaction` | `text` | `YES` | `` |
| `register` | `jsonb` | `YES` | `` |
| `reference` | `text` | `YES` | `` |
| `updatedBy` | `text` | `YES` | `` |
| `amount` | `numeric` | `YES` | `` |

### `doorloop_raw_vendor_credits`
**Primary Key:** `id`
**Indexes:** 1

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `text` | `NO` | `` |

### `doorloop_raw_vendors`
**Primary Key:** `id`
**Indexes:** 1

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `text` | `NO` | `` |
| `data` | `jsonb` | `YES` | `` |
| `source_endpoint` | `text` | `YES` | `` |
| `inserted_at` | `timestamptz` | `YES` | `now()` |
| `outgoingEPay` | `jsonb` | `YES` | `` |
| `companyName` | `text` | `YES` | `` |
| `firstName` | `text` | `YES` | `` |
| `active` | `bool` | `YES` | `` |
| `createdBy` | `text` | `YES` | `` |
| `services` | `jsonb` | `YES` | `` |
| `createdAt` | `timestamptz` | `YES` | `` |
| `emails` | `jsonb` | `YES` | `` |
| `batch` | `text` | `YES` | `` |
| `fullName` | `text` | `YES` | `` |
| `jobTitle` | `text` | `YES` | `` |
| `updatedAt` | `timestamptz` | `YES` | `` |
| `balance` | `numeric` | `YES` | `` |
| `primaryAddress` | `jsonb` | `YES` | `` |
| `properties` | `jsonb` | `YES` | `` |
| `e164PhoneMobileNumber` | `text` | `YES` | `` |
| `phones` | `jsonb` | `YES` | `` |
| `company` | `bool` | `YES` | `` |
| `alternateAddress` | `jsonb` | `YES` | `` |
| `name` | `text` | `YES` | `` |
| `updatedBy` | `text` | `YES` | `` |
| `accounts` | `jsonb` | `YES` | `` |
| `conversationWelcomeSmsSentAt` | `timestamptz` | `YES` | `` |
| `lastName` | `text` | `YES` | `` |

### `doorloop_raw_work_orders`
**Primary Key:** `id`
**Indexes:** 1

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `text` | `NO` | `` |
| `data` | `jsonb` | `YES` | `` |
| `source_endpoint` | `text` | `YES` | `` |
| `inserted_at` | `timestamptz` | `YES` | `now()` |

### `eviction_proceedings`
**Primary Key:** `id, id, id`
**Foreign Keys:** 1
**Indexes:** 2

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `int8` | `NO` | `` |
| `case_number` | `text` | `YES` | `` |
| `lease_id` | `int8` | `YES` | `` |
| `tenant_id` | `int8` | `YES` | `` |
| `status` | `text` | `YES` | `` |
| `filing_date` | `date` | `YES` | `` |
| `judgement_date` | `date` | `YES` | `` |
| `judgement_amount` | `numeric` | `YES` | `` |
| `attorney_id` | `text` | `YES` | `` |
| `notes` | `text` | `YES` | `` |
| `created_at` | `timestamptz` | `NO` | `timezone('utc'::text, now())` |
| `updated_at` | `timestamptz` | `NO` | `timezone('utc'::text, now())` |

### `file_assets`
**Primary Key:** `id, id`
**Indexes:** 3

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `int8` | `NO` | `` |
| `supabase_entity_id` | `int8` | `NO` | `` |
| `entity_type` | `text` | `NO` | `` |
| `dropbox_path` | `text` | `NO` | `` |
| `file_name` | `text` | `NO` | `` |
| `mime_type` | `text` | `YES` | `` |
| `size` | `int8` | `YES` | `` |
| `created_by_user_id` | `int8` | `YES` | `` |
| `shared_link_url` | `text` | `YES` | `` |
| `shared_link_expires_at` | `timestamptz` | `YES` | `` |
| `created_at` | `timestamptz` | `NO` | `now()` |

### `file_sync_audit`
**Primary Key:** `id, id, id, id`
**Indexes:** 3

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `int8` | `NO` | `` |
| `timestamp` | `timestamptz` | `NO` | `now()` |
| `event_type` | `text` | `NO` | `` |
| `dropbox_path` | `text` | `NO` | `` |
| `status` | `text` | `NO` | `` |
| `error_message` | `text` | `YES` | `` |
| `triggered_by` | `text` | `NO` | `` |

### `files`
**Primary Key:** `id, id`
**Indexes:** 2

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `int4` | `NO` | `nextval('files_id_seq'::regclass)` |
| `doorloop_id` | `varchar` | `NO` | `` |
| `name` | `text` | `YES` | `` |
| `notes` | `text` | `YES` | `` |
| `resource_id_dl` | `varchar` | `YES` | `` |
| `resource_type` | `text` | `YES` | `` |
| `size_bytes` | `int8` | `YES` | `` |
| `mime_type` | `text` | `YES` | `` |
| `download_url` | `text` | `YES` | `` |
| `created_by_dl` | `varchar` | `YES` | `` |
| `created_at` | `timestamptz` | `YES` | `` |
| `updated_at` | `timestamptz` | `YES` | `` |

### `kpi_summary`
**Primary Key:** `id`
**Indexes:** 1

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `int8` | `NO` | `` |
| `kpis` | `jsonb` | `NO` | `` |
| `updated_at` | `timestamptz` | `NO` | `now()` |

### `lease_charges`
**Primary Key:** `id, id`
**Indexes:** 2

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `int4` | `NO` | `nextval('lease_charges_id_seq'::regclass)` |
| `doorloop_id` | `varchar` | `NO` | `` |
| `amount_cents` | `int8` | `YES` | `` |
| `memo` | `text` | `YES` | `` |
| `date` | `date` | `YES` | `` |
| `lease_id_dl` | `varchar` | `YES` | `` |
| `account_id_dl` | `varchar` | `YES` | `` |
| `created_at` | `timestamptz` | `YES` | `` |
| `updated_at` | `timestamptz` | `YES` | `` |

### `lease_credits`
**Primary Key:** `id, id`
**Indexes:** 2

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `int4` | `NO` | `nextval('lease_credits_id_seq'::regclass)` |
| `doorloop_id` | `varchar` | `NO` | `` |
| `amount_cents` | `int8` | `YES` | `` |
| `memo` | `text` | `YES` | `` |
| `date` | `date` | `YES` | `` |
| `lease_id_dl` | `varchar` | `YES` | `` |
| `account_id_dl` | `varchar` | `YES` | `` |
| `created_at` | `timestamptz` | `YES` | `` |
| `updated_at` | `timestamptz` | `YES` | `` |

### `lease_payments`
**Primary Key:** `id, id`
**Indexes:** 2

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `int4` | `NO` | `nextval('lease_payments_id_seq'::regclass)` |
| `doorloop_id` | `varchar` | `NO` | `` |
| `amount_cents` | `int8` | `YES` | `` |
| `payment_date` | `date` | `YES` | `` |
| `status` | `text` | `YES` | `` |
| `payment_method` | `text` | `YES` | `` |
| `lease_id_dl` | `varchar` | `YES` | `` |
| `tenant_id_dl` | `varchar` | `YES` | `` |
| `account_id_dl` | `varchar` | `YES` | `` |
| `created_at` | `timestamptz` | `YES` | `` |
| `updated_at` | `timestamptz` | `YES` | `` |

### `lease_tenants`
**Primary Key:** `lease_id, lease_id, lease_id, tenant_id, tenant_id, tenant_id`
**Foreign Keys:** 2
**Indexes:** 1

| Column | Type | Nullable | Default |
|---|---|---|---|
| `lease_id` | `int8` | `NO` | `` |
| `tenant_id` | `int8` | `NO` | `` |

### `leases`
**Primary Key:** `id, id, id, id, id, id`
**Foreign Keys:** 3
**Indexes:** 9

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `int8` | `NO` | `` |
| `property_id` | `int8` | `NO` | `` |
| `unit_id` | `int8` | `YES` | `` |
| `primary_tenant_id` | `int8` | `YES` | `` |
| `start_date` | `date` | `NO` | `` |
| `end_date` | `date` | `NO` | `` |
| `rent_cents` | `int4` | `NO` | `` |
| `deposit_cents` | `int4` | `YES` | `0` |
| `status` | `text` | `NO` | `` |
| `doorloop_id` | `text` | `YES` | `` |
| `created_at` | `timestamptz` | `NO` | `now()` |
| `updated_at` | `timestamptz` | `NO` | `now()` |

### `legal_case_import_staging`
**Primary Key:** `id`
**Indexes:** 1

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `uuid` | `NO` | `gen_random_uuid()` |
| `uploaded_at` | `timestamptz` | `YES` | `now()` |
| `uploaded_by` | `text` | `YES` | `` |
| `original_filename` | `text` | `YES` | `` |
| `row_number` | `int4` | `NO` | `` |
| `raw_data` | `jsonb` | `NO` | `` |
| `status` | `text` | `YES` | `'pending'::text` |
| `validation_errors` | `jsonb` | `YES` | `` |
| `processed_at` | `timestamptz` | `YES` | `` |

### `legal_cases_import_staging`
**Primary Key:** `id`
**Indexes:** 1

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `int8` | `NO` | `nextval('legal_cases_import_staging_id_seq'::regclass)` |
| `tenant_name` | `varchar` | `NO` | `` |
| `property_address` | `varchar` | `YES` | `` |
| `case_type` | `varchar` | `YES` | `` |
| `lease_start` | `date` | `YES` | `` |
| `lease_end` | `date` | `YES` | `` |
| `amount_claimed` | `numeric` | `YES` | `` |
| `notes` | `text` | `YES` | `` |
| `status` | `varchar` | `YES` | `'pending'::character varying` |
| `source_file_name` | `varchar` | `YES` | `` |
| `import_errors` | `jsonb` | `YES` | `` |
| `resolved_property_id` | `int4` | `YES` | `` |
| `resolved_tenant_id` | `int4` | `YES` | `` |
| `resolved_lease_id` | `int4` | `YES` | `` |
| `created_at` | `timestamp` | `YES` | `CURRENT_TIMESTAMP` |
| `updated_at` | `timestamp` | `YES` | `CURRENT_TIMESTAMP` |

### `notes`
**Primary Key:** `id, id`
**Indexes:** 2

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `int4` | `NO` | `nextval('notes_id_seq'::regclass)` |
| `doorloop_id` | `varchar` | `NO` | `` |
| `title` | `text` | `YES` | `` |
| `body` | `text` | `YES` | `` |
| `resource_id_dl` | `varchar` | `YES` | `` |
| `resource_type` | `text` | `YES` | `` |
| `created_by_dl` | `varchar` | `YES` | `` |
| `created_at` | `timestamptz` | `YES` | `` |
| `updated_at` | `timestamptz` | `YES` | `` |

### `owners`
**Primary Key:** `id, id`
**Indexes:** 2

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `int4` | `NO` | `nextval('owners_id_seq'::regclass)` |
| `doorloop_id` | `varchar` | `NO` | `` |
| `first_name` | `text` | `YES` | `` |
| `last_name` | `text` | `YES` | `` |
| `full_name` | `text` | `YES` | `` |
| `display_name` | `text` | `YES` | `` |
| `company_name` | `text` | `YES` | `` |
| `notes` | `text` | `YES` | `` |
| `active` | `bool` | `YES` | `true` |
| `management_start_date` | `date` | `YES` | `` |
| `management_end_date` | `date` | `YES` | `` |
| `created_at` | `timestamptz` | `YES` | `` |
| `updated_at` | `timestamptz` | `YES` | `` |

### `portfolios`
**Primary Key:** `id, id`
**Indexes:** 2

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `int4` | `NO` | `nextval('portfolios_id_seq'::regclass)` |
| `doorloop_id` | `varchar` | `NO` | `` |
| `name` | `text` | `YES` | `` |
| `created_at` | `timestamptz` | `YES` | `` |
| `updated_at` | `timestamptz` | `YES` | `` |

### `properties`
**Primary Key:** `id, id`
**Indexes:** 2

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `int8` | `NO` | `` |
| `doorloop_id` | `text` | `YES` | `` |
| `name` | `text` | `YES` | `` |
| `type` | `text` | `YES` | `` |
| `class` | `text` | `YES` | `` |
| `active` | `bool` | `YES` | `` |
| `address_street1` | `text` | `YES` | `` |
| `address_city` | `text` | `YES` | `` |
| `address_state` | `text` | `YES` | `` |
| `address_zip` | `text` | `YES` | `` |
| `created_at` | `timestamptz` | `YES` | `now()` |
| `updated_at` | `timestamptz` | `YES` | `now()` |
| `total_sqft` | `numeric` | `YES` | `` |
| `unit_count` | `int4` | `YES` | `` |
| `occupied_unit_count` | `int4` | `YES` | `` |
| `vacant_unit_count` | `int4` | `YES` | `` |
| `occupancy_rate` | `numeric` | `YES` | `` |

### `property_owners`
**Primary Key:** `property_id, property_id, property_id, owner_id, owner_id, owner_id`
**Foreign Keys:** 2
**Indexes:** 1

| Column | Type | Nullable | Default |
|---|---|---|---|
| `property_id` | `int8` | `NO` | `` |
| `owner_id` | `int8` | `NO` | `` |

### `sql_execution_logs`
**Primary Key:** `id`
**Indexes:** 1

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `int8` | `NO` | `` |
| `executed_at` | `timestamptz` | `NO` | `now()` |
| `sql_file` | `text` | `YES` | `` |
| `sql_content` | `text` | `NO` | `` |
| `execution_time_ms` | `float8` | `YES` | `` |
| `status` | `text` | `NO` | `` |
| `error_message` | `text` | `YES` | `` |
| `error_detail` | `text` | `YES` | `` |

### `tasks`
**Primary Key:** `id, id`
**Indexes:** 2

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `int4` | `NO` | `nextval('tasks_id_seq'::regclass)` |
| `doorloop_id` | `varchar` | `NO` | `` |
| `type` | `text` | `YES` | `` |
| `subject` | `text` | `YES` | `` |
| `description` | `text` | `YES` | `` |
| `status` | `text` | `YES` | `` |
| `priority` | `text` | `YES` | `` |
| `due_date` | `date` | `YES` | `` |
| `property_id_dl` | `varchar` | `YES` | `` |
| `unit_id_dl` | `varchar` | `YES` | `` |
| `tenant_id_dl` | `varchar` | `YES` | `` |
| `owner_id_dl` | `varchar` | `YES` | `` |
| `user_id_dl` | `varchar` | `YES` | `` |
| `vendor_id_dl` | `varchar` | `YES` | `` |
| `created_at` | `timestamptz` | `YES` | `` |
| `updated_at` | `timestamptz` | `YES` | `` |

### `tenants`
**Primary Key:** `id, id`
**Indexes:** 2

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `int4` | `NO` | `nextval('tenants_id_seq'::regclass)` |
| `doorloop_id` | `varchar` | `NO` | `` |
| `first_name` | `text` | `YES` | `` |
| `last_name` | `text` | `YES` | `` |
| `full_name` | `text` | `YES` | `` |
| `display_name` | `text` | `YES` | `` |
| `date_of_birth` | `date` | `YES` | `` |
| `company_name` | `text` | `YES` | `` |
| `notes` | `text` | `YES` | `` |
| `type` | `text` | `YES` | `` |
| `credit_score` | `int4` | `YES` | `` |
| `created_at` | `timestamptz` | `YES` | `` |
| `updated_at` | `timestamptz` | `YES` | `` |

### `units`
**Primary Key:** `id, id`
**Indexes:** 4

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `int8` | `NO` | `` |
| `doorloop_id` | `text` | `YES` | `` |
| `unit_number` | `text` | `YES` | `` |
| `beds` | `numeric` | `YES` | `` |
| `baths` | `numeric` | `YES` | `` |
| `sq_ft` | `numeric` | `YES` | `` |
| `rent_amount` | `numeric` | `YES` | `` |
| `doorloop_property_id` | `text` | `YES` | `` |
| `created_at` | `timestamptz` | `YES` | `now()` |
| `updated_at` | `timestamptz` | `YES` | `now()` |
| `status` | `text` | `YES` | `` |

### `users`
**Primary Key:** `id, id`
**Indexes:** 2

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `int4` | `NO` | `nextval('users_id_seq'::regclass)` |
| `doorloop_id` | `varchar` | `NO` | `` |
| `first_name` | `text` | `YES` | `` |
| `last_name` | `text` | `YES` | `` |
| `full_name` | `text` | `YES` | `` |
| `email` | `text` | `YES` | `` |
| `role` | `text` | `YES` | `` |
| `active` | `bool` | `YES` | `true` |
| `last_seen_at` | `timestamptz` | `YES` | `` |
| `created_at` | `timestamptz` | `YES` | `` |
| `updated_at` | `timestamptz` | `YES` | `` |

### `vendors`
**Primary Key:** `id, id`
**Indexes:** 2

| Column | Type | Nullable | Default |
|---|---|---|---|
| `id` | `int4` | `NO` | `nextval('vendors_id_seq'::regclass)` |
| `doorloop_id` | `varchar` | `NO` | `` |
| `first_name` | `text` | `YES` | `` |
| `last_name` | `text` | `YES` | `` |
| `full_name` | `text` | `YES` | `` |
| `display_name` | `text` | `YES` | `` |
| `company_name` | `text` | `YES` | `` |
| `notes` | `text` | `YES` | `` |
| `active` | `bool` | `YES` | `true` |
| `balance_cents` | `int8` | `YES` | `` |
| `created_at` | `timestamptz` | `YES` | `` |
| `updated_at` | `timestamptz` | `YES` | `` |


## Views

- `get_full_work_orders_view` (VIEW)
- `normalized_leases` (VIEW)
- `normalized_owners` (VIEW)
- `normalized_payments` (VIEW)
- `normalized_properties` (VIEW)
- `normalized_tenants` (VIEW)
- `normalized_units` (VIEW)
- `normalized_vendors` (VIEW)
- `normalized_work_orders` (VIEW)
- `sync_leases` (VIEW)
- `sync_owners` (VIEW)
- `sync_payments` (VIEW)
- `sync_properties` (VIEW)
- `sync_tenants` (VIEW)
- `sync_vendors` (VIEW)
- `sync_work_orders` (VIEW)

## Enums


## Functions

- `add_column_if_not_exists` returns `void`
- `add_service_role_policy_to_doorloop_tables` returns `void`
- `columns_in_table` returns `TABLE(column_name text, data_type text)`
- `exec_sql` returns `jsonb`
- `execute_sql` returns `jsonb`
- `execute_sql_v2` returns `jsonb`
- `export_schema_manifest` returns `jsonb`
- `get_table_columns_rpc` returns `TABLE(column_name text, data_type text)`
- `healthcheck` returns `text`
- `log_sql_execution` returns `void`
- `log_sql_execution` returns `void`
- `touch_leases_updated_at` returns `trigger`

## Triggers

- `trg_touch_leases` on `leases`