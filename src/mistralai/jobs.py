"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from datetime import datetime
from mistralai import models, utils
from mistralai._hooks import HookContext
from mistralai.types import OptionalNullable, UNSET
from mistralai.utils import get_security_from_env
from typing import List, Optional, Union

class Jobs(BaseSDK):
    
    
    def list(
        self, *,
        page: Optional[int] = 0,
        page_size: Optional[int] = 100,
        model: OptionalNullable[str] = UNSET,
        created_after: OptionalNullable[datetime] = UNSET,
        created_by_me: Optional[bool] = False,
        status: OptionalNullable[models.QueryParamStatus] = UNSET,
        wandb_project: OptionalNullable[str] = UNSET,
        wandb_name: OptionalNullable[str] = UNSET,
        suffix: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[models.JobsOut]:
        r"""Get Fine Tuning Jobs

        Get a list of fine-tuning jobs for your organization and user.

        :param page: The page number of the results to be returned.
        :param page_size: The number of items to return per page.
        :param model: The model name used for fine-tuning to filter on. When set, the other results are not displayed.
        :param created_after: The date/time to filter on. When set, the results for previous creation times are not displayed.
        :param created_by_me: When set, only return results for jobs created by the API caller. Other results are not displayed.
        :param status: The current job state to filter on. When set, the other results are not displayed.
        :param wandb_project: The Weights and Biases project to filter on. When set, the other results are not displayed.
        :param wandb_name: The Weight and Biases run name to filter on. When set, the other results are not displayed.
        :param suffix: The model suffix to filter on. When set, the other results are not displayed.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        request = models.JobsAPIRoutesFineTuningGetFineTuningJobsRequest(
            page=page,
            page_size=page_size,
            model=model,
            created_after=created_after,
            created_by_me=created_by_me,
            status=status,
            wandb_project=wandb_project,
            wandb_name=wandb_name,
            suffix=suffix,
        )
        
        req = self.build_request(
            method="GET",
            path="/v1/fine_tuning/jobs",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="jobs_api_routes_fine_tuning_get_fine_tuning_jobs", oauth2_scopes=[], security_source=get_security_from_env(self.sdk_configuration.security, models.Security)),
            request=req,
            error_status_codes=["4XX","5XX"],
            retry_config=retry_config
        )
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.JobsOut])
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    async def list_async(
        self, *,
        page: Optional[int] = 0,
        page_size: Optional[int] = 100,
        model: OptionalNullable[str] = UNSET,
        created_after: OptionalNullable[datetime] = UNSET,
        created_by_me: Optional[bool] = False,
        status: OptionalNullable[models.QueryParamStatus] = UNSET,
        wandb_project: OptionalNullable[str] = UNSET,
        wandb_name: OptionalNullable[str] = UNSET,
        suffix: OptionalNullable[str] = UNSET,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[models.JobsOut]:
        r"""Get Fine Tuning Jobs

        Get a list of fine-tuning jobs for your organization and user.

        :param page: The page number of the results to be returned.
        :param page_size: The number of items to return per page.
        :param model: The model name used for fine-tuning to filter on. When set, the other results are not displayed.
        :param created_after: The date/time to filter on. When set, the results for previous creation times are not displayed.
        :param created_by_me: When set, only return results for jobs created by the API caller. Other results are not displayed.
        :param status: The current job state to filter on. When set, the other results are not displayed.
        :param wandb_project: The Weights and Biases project to filter on. When set, the other results are not displayed.
        :param wandb_name: The Weight and Biases run name to filter on. When set, the other results are not displayed.
        :param suffix: The model suffix to filter on. When set, the other results are not displayed.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        request = models.JobsAPIRoutesFineTuningGetFineTuningJobsRequest(
            page=page,
            page_size=page_size,
            model=model,
            created_after=created_after,
            created_by_me=created_by_me,
            status=status,
            wandb_project=wandb_project,
            wandb_name=wandb_name,
            suffix=suffix,
        )
        
        req = self.build_request(
            method="GET",
            path="/v1/fine_tuning/jobs",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="jobs_api_routes_fine_tuning_get_fine_tuning_jobs", oauth2_scopes=[], security_source=get_security_from_env(self.sdk_configuration.security, models.Security)),
            request=req,
            error_status_codes=["4XX","5XX"],
            retry_config=retry_config
        )
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.JobsOut])
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    def create(
        self, *,
        model: models.FineTuneableModel,
        hyperparameters: Union[models.TrainingParametersIn, models.TrainingParametersInTypedDict],
        training_files: Optional[Union[List[models.TrainingFile], List[models.TrainingFileTypedDict]]] = None,
        validation_files: OptionalNullable[List[str]] = UNSET,
        suffix: OptionalNullable[str] = UNSET,
        integrations: OptionalNullable[Union[List[models.WandbIntegration], List[models.WandbIntegrationTypedDict]]] = UNSET,
        repositories: Optional[Union[List[models.GithubRepositoryIn], List[models.GithubRepositoryInTypedDict]]] = None,
        auto_start: Optional[bool] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[models.JobsAPIRoutesFineTuningCreateFineTuningJobResponse]:
        r"""Create Fine Tuning Job

        Create a new fine-tuning job, it will be queued for processing.

        :param model: The name of the model to fine-tune.
        :param hyperparameters: The fine-tuning hyperparameter settings used in a fine-tune job.
        :param training_files: 
        :param validation_files: A list containing the IDs of uploaded files that contain validation data. If you provide these files, the data is used to generate validation metrics periodically during fine-tuning. These metrics can be viewed in `checkpoints` when getting the status of a running fine-tuning job. The same data should not be present in both train and validation files.
        :param suffix: A string that will be added to your fine-tuning model name. For example, a suffix of \"my-great-model\" would produce a model name like `ft:open-mistral-7b:my-great-model:xxx...`
        :param integrations: A list of integrations to enable for your fine-tuning job.
        :param repositories: 
        :param auto_start: This field will be required in a future release.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        request = models.JobIn(
            model=model,
            training_files=utils.get_pydantic_model(training_files, Optional[List[models.TrainingFile]]),
            validation_files=validation_files,
            hyperparameters=utils.get_pydantic_model(hyperparameters, models.TrainingParametersIn),
            suffix=suffix,
            integrations=utils.get_pydantic_model(integrations, OptionalNullable[List[models.WandbIntegration]]),
            repositories=utils.get_pydantic_model(repositories, Optional[List[models.GithubRepositoryIn]]),
            auto_start=auto_start,
        )
        
        req = self.build_request(
            method="POST",
            path="/v1/fine_tuning/jobs",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request, False, False, "json", models.JobIn),
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="jobs_api_routes_fine_tuning_create_fine_tuning_job", oauth2_scopes=[], security_source=get_security_from_env(self.sdk_configuration.security, models.Security)),
            request=req,
            error_status_codes=["4XX","5XX"],
            retry_config=retry_config
        )
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.JobsAPIRoutesFineTuningCreateFineTuningJobResponse])
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    async def create_async(
        self, *,
        model: models.FineTuneableModel,
        hyperparameters: Union[models.TrainingParametersIn, models.TrainingParametersInTypedDict],
        training_files: Optional[Union[List[models.TrainingFile], List[models.TrainingFileTypedDict]]] = None,
        validation_files: OptionalNullable[List[str]] = UNSET,
        suffix: OptionalNullable[str] = UNSET,
        integrations: OptionalNullable[Union[List[models.WandbIntegration], List[models.WandbIntegrationTypedDict]]] = UNSET,
        repositories: Optional[Union[List[models.GithubRepositoryIn], List[models.GithubRepositoryInTypedDict]]] = None,
        auto_start: Optional[bool] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[models.JobsAPIRoutesFineTuningCreateFineTuningJobResponse]:
        r"""Create Fine Tuning Job

        Create a new fine-tuning job, it will be queued for processing.

        :param model: The name of the model to fine-tune.
        :param hyperparameters: The fine-tuning hyperparameter settings used in a fine-tune job.
        :param training_files: 
        :param validation_files: A list containing the IDs of uploaded files that contain validation data. If you provide these files, the data is used to generate validation metrics periodically during fine-tuning. These metrics can be viewed in `checkpoints` when getting the status of a running fine-tuning job. The same data should not be present in both train and validation files.
        :param suffix: A string that will be added to your fine-tuning model name. For example, a suffix of \"my-great-model\" would produce a model name like `ft:open-mistral-7b:my-great-model:xxx...`
        :param integrations: A list of integrations to enable for your fine-tuning job.
        :param repositories: 
        :param auto_start: This field will be required in a future release.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        request = models.JobIn(
            model=model,
            training_files=utils.get_pydantic_model(training_files, Optional[List[models.TrainingFile]]),
            validation_files=validation_files,
            hyperparameters=utils.get_pydantic_model(hyperparameters, models.TrainingParametersIn),
            suffix=suffix,
            integrations=utils.get_pydantic_model(integrations, OptionalNullable[List[models.WandbIntegration]]),
            repositories=utils.get_pydantic_model(repositories, Optional[List[models.GithubRepositoryIn]]),
            auto_start=auto_start,
        )
        
        req = self.build_request(
            method="POST",
            path="/v1/fine_tuning/jobs",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request, False, False, "json", models.JobIn),
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="jobs_api_routes_fine_tuning_create_fine_tuning_job", oauth2_scopes=[], security_source=get_security_from_env(self.sdk_configuration.security, models.Security)),
            request=req,
            error_status_codes=["4XX","5XX"],
            retry_config=retry_config
        )
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.JobsAPIRoutesFineTuningCreateFineTuningJobResponse])
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    def get(
        self, *,
        job_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[models.DetailedJobOut]:
        r"""Get Fine Tuning Job

        Get a fine-tuned job details by its UUID.

        :param job_id: The ID of the job to analyse.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        request = models.JobsAPIRoutesFineTuningGetFineTuningJobRequest(
            job_id=job_id,
        )
        
        req = self.build_request(
            method="GET",
            path="/v1/fine_tuning/jobs/{job_id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="jobs_api_routes_fine_tuning_get_fine_tuning_job", oauth2_scopes=[], security_source=get_security_from_env(self.sdk_configuration.security, models.Security)),
            request=req,
            error_status_codes=["4XX","5XX"],
            retry_config=retry_config
        )
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.DetailedJobOut])
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    async def get_async(
        self, *,
        job_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[models.DetailedJobOut]:
        r"""Get Fine Tuning Job

        Get a fine-tuned job details by its UUID.

        :param job_id: The ID of the job to analyse.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        request = models.JobsAPIRoutesFineTuningGetFineTuningJobRequest(
            job_id=job_id,
        )
        
        req = self.build_request(
            method="GET",
            path="/v1/fine_tuning/jobs/{job_id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="jobs_api_routes_fine_tuning_get_fine_tuning_job", oauth2_scopes=[], security_source=get_security_from_env(self.sdk_configuration.security, models.Security)),
            request=req,
            error_status_codes=["4XX","5XX"],
            retry_config=retry_config
        )
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.DetailedJobOut])
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    def cancel(
        self, *,
        job_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[models.DetailedJobOut]:
        r"""Cancel Fine Tuning Job

        Request the cancellation of a fine tuning job.

        :param job_id: The ID of the job to cancel.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        request = models.JobsAPIRoutesFineTuningCancelFineTuningJobRequest(
            job_id=job_id,
        )
        
        req = self.build_request(
            method="POST",
            path="/v1/fine_tuning/jobs/{job_id}/cancel",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="jobs_api_routes_fine_tuning_cancel_fine_tuning_job", oauth2_scopes=[], security_source=get_security_from_env(self.sdk_configuration.security, models.Security)),
            request=req,
            error_status_codes=["4XX","5XX"],
            retry_config=retry_config
        )
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.DetailedJobOut])
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    async def cancel_async(
        self, *,
        job_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[models.DetailedJobOut]:
        r"""Cancel Fine Tuning Job

        Request the cancellation of a fine tuning job.

        :param job_id: The ID of the job to cancel.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        request = models.JobsAPIRoutesFineTuningCancelFineTuningJobRequest(
            job_id=job_id,
        )
        
        req = self.build_request(
            method="POST",
            path="/v1/fine_tuning/jobs/{job_id}/cancel",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="jobs_api_routes_fine_tuning_cancel_fine_tuning_job", oauth2_scopes=[], security_source=get_security_from_env(self.sdk_configuration.security, models.Security)),
            request=req,
            error_status_codes=["4XX","5XX"],
            retry_config=retry_config
        )
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.DetailedJobOut])
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    def start(
        self, *,
        job_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[models.DetailedJobOut]:
        r"""Start Fine Tuning Job

        Request the start of a validated fine tuning job.

        :param job_id: 
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        request = models.JobsAPIRoutesFineTuningStartFineTuningJobRequest(
            job_id=job_id,
        )
        
        req = self.build_request(
            method="POST",
            path="/v1/fine_tuning/jobs/{job_id}/start",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="jobs_api_routes_fine_tuning_start_fine_tuning_job", oauth2_scopes=[], security_source=get_security_from_env(self.sdk_configuration.security, models.Security)),
            request=req,
            error_status_codes=["4XX","5XX"],
            retry_config=retry_config
        )
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.DetailedJobOut])
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    async def start_async(
        self, *,
        job_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[models.DetailedJobOut]:
        r"""Start Fine Tuning Job

        Request the start of a validated fine tuning job.

        :param job_id: 
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        request = models.JobsAPIRoutesFineTuningStartFineTuningJobRequest(
            job_id=job_id,
        )
        
        req = self.build_request(
            method="POST",
            path="/v1/fine_tuning/jobs/{job_id}/start",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="jobs_api_routes_fine_tuning_start_fine_tuning_job", oauth2_scopes=[], security_source=get_security_from_env(self.sdk_configuration.security, models.Security)),
            request=req,
            error_status_codes=["4XX","5XX"],
            retry_config=retry_config
        )
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.DetailedJobOut])
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
