# from hks_backend.celery import app
# from opportunity.models import Opportunity

# from .leadscoring import LeadScoringPricing, LeadScoringSales
# from utils import data_frame_for_ga_data, data_frame_for_opportunity, get_ga_data

import pickle
from sklearn import model_selection
import utils
from leadscoring import Preprocessing, Scoring

class Opportunity(object):
    """dummy class for opportunity object"""
    def __init__(self, id):
        self.id = id
        self.pk = id

# @app.task(ignore_result=True)
def calculate_lead_scores(opportunity_id, iteration=1, max_iterations=3):

    # training:
    opps = Preprocessing(None, utils.x_columns, utils.y_column,
                         utils.opps_convert_dict, utils.opps_drop_dict, utils.opps_replace_dict,
                         utils.opps_feature_dict)
    opps.data_frame_for_opportunity(single_opp=False)
    opps.drop()
    opps.replace()
    opps.convert()
    opps.feature()
    pickle.dump(opps.df, open('static/df', 'wb'))
    opps_data = pickle.load(open('static/df', 'rb'))

    # testing:

    ls_sales = Scoring(method='classification', df=opps_data, x_columns=utils.x_columns, y_column=utils.y_column)
    ls_sales.get_X()
    ls_sales.get_y()
    ls_sales.create_model()

    print(ls_sales.feature_columns_)

    print(model_selection.cross_val_score(ls_sales.model, ls_sales.X, ls_sales.y, scoring='recall', cv=10, n_jobs=1))


    # scoring:

    # opportunity = Opportunity.objects.select_related('trackinginfo').get(pk=opportunity_id)
    opportunity = Opportunity(opportunity_id)

    # get pandas data frame for opportunity:
    opps = Preprocessing(opportunity, utils.x_columns, utils.y_column,
                         utils.opps_convert_dict, utils.opps_drop_dict, utils.opps_replace_dict,
                         utils.opps_feature_dict)
    opps.data_frame_for_opportunity(single_opp=True)
    # opps.drop()  # only training
    opps.replace()
    opps.convert()
    opps.feature()

    ga_oppid = Preprocessing(opportunity, convert_dict=utils.ga_convert_dict,
                             replace_dict=utils.ga_replace_dict,
                             feature_dict=utils.ga_feature_dict,
                             ga_metrics=utils.ga_metrics,
                             ga_dims=utils.ga_oppid_dims)
    # ga_oppid.get_ga_data(opportunity)

    ga_clientid = Preprocessing(opportunity, convert_dict=utils.ga_convert_dict,
                             replace_dict=utils.ga_replace_dict,
                             feature_dict=utils.ga_feature_dict,
                             ga_metrics=utils.ga_metrics,
                             ga_dims=utils.ga_clientid_dims)


    ls_sales = Scoring(method='classification', df=opps.df, x_columns=utils.x_columns, y_column=utils.y_column)

    ls_sales.get_X()
    ls_sales.get_y()
    ls_sales.create_model()

    ls_pricing = Scoring(method='regression', df=opps.df, x_columns=utils.x_columns, y_column=utils.y_column)

    # get analytics data from API
    # ga_userid_data, ga_clientid_data = get_ga_data(opportunity)

    # transform analytics data to pandas data frame
    # ga_userid_raw = data_frame_for_ga_data(ga_userid_data)
    # ga_clientid_raw = data_frame_for_ga_data(ga_clientid_data)

    # Google analytics data might not be available right away after the lead was created
    # if we don't get data, we should try the scoring again 5 minutes later
    # we repeat this until we have data or until we tried often enough (max_iterations)
    # if ga_clientid_raw is None or ga_userid_raw is None:
    #     if iteration < max_iterations:
    #         calculate_lead_scores.apply_async(
    #             args=[opportunity_id],
    #             kwargs={'iteration': iteration + 1},
    #             countdown=300
    #         )

    # ls_sales = LeadScoringSales()
    # sales_score = ls_sales.score_lead(opps_raw, ga_clientid_raw, ga_userid_raw, ga_gclid_raw)
    #
    # ls_pricing = LeadScoringPricing()
    # pricing_score = ls_pricing.score_lead(opps_raw, ga_clientid_raw, ga_userid_raw, ga_gclid_raw)
    # if pricing_score is not None:
    #     pricing_score_min, pricing_score_max = pricing_score
    # else:
    #     pricing_score_min, pricing_score_max = [None, None]
    #
    # opportunity.sales_score = sales_score
    # opportunity.pricing_score_min = pricing_score_min
    # opportunity.pricing_score_max = pricing_score_max
    # opportunity.sales_score_method_used = ls_sales.calc_version
    # opportunity.pricing_score_method_used = ls_pricing.calc_version
    # opportunity.save(update_fields=['sales_score', 'sales_score_method_used',
    #                                 'pricing_score_min', 'pricing_score_max',
    #                                 'pricing_score_method_used'])



if __name__ == '__main__':
    calculate_lead_scores(185917)
