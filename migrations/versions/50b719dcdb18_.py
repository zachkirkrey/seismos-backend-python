"""empty message

Revision ID: 50b719dcdb18
Revises: 
Create Date: 2022-03-13 04:26:37.879592

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "50b719dcdb18"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "active_data",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("stage_id", sa.Integer(), nullable=False),
        sa.Column("amplitude", sa.Integer(), nullable=False),
        sa.Column("frequency", sa.Float(), nullable=False),
        sa.Column("offset", sa.Integer(), nullable=False),
        sa.Column("period", sa.Integer(), nullable=False),
        sa.Column("wave_type", sa.String(length=50), nullable=True),
        sa.Column(
            "post_frac_start_time", sa.Numeric(precision=25, scale=10), nullable=True
        ),
        sa.Column(
            "post_frac_end_time", sa.Numeric(precision=25, scale=10), nullable=True
        ),
        sa.Column(
            "pre_frac_start_time", sa.Numeric(precision=25, scale=10), nullable=True
        ),
        sa.Column(
            "pre_frac_end_time", sa.Numeric(precision=25, scale=10), nullable=True
        ),
        sa.Column(
            "pre_frac_num_pulse", sa.Numeric(precision=25, scale=10), nullable=True
        ),
        sa.Column(
            "post_frac_num_pulse", sa.Numeric(precision=25, scale=10), nullable=True
        ),
        sa.Column("pre_frac_pulse_note", sa.String(length=255), nullable=True),
        sa.Column("post_frac_pulse_note", sa.String(length=255), nullable=True),
        sa.Column("additional_note", sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "basin_name",
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("basin_name", sa.Text(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "chem_fluids",
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("id", sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column("stage_id", sa.Integer(), nullable=True),
        sa.Column("fluid_type_name", sa.Integer(), nullable=True),
        sa.Column("chem_trade_name", sa.Text(), nullable=True),
        sa.Column("chem_name", sa.Text(), nullable=True),
        sa.Column("volume", sa.Float(), nullable=True),
        sa.Column("volume_unit", sa.Text(), nullable=True),
        sa.Column("volume_concentration", sa.Float(), nullable=True),
        sa.Column("volume_concentration_unit", sa.Text(), nullable=True),
        sa.Column("dry_total", sa.Float(), nullable=True),
        sa.Column("dry_total_unit", sa.Text(), nullable=True),
        sa.Column("dry_concentration", sa.Float(), nullable=True),
        sa.Column("dry_concentration_unit", sa.Text(), nullable=True),
        sa.Column("acid", sa.Float(), nullable=True),
        sa.Column("acid_unit", sa.Text(), nullable=True),
        sa.Column("clay_stabilizer", sa.Float(), nullable=True),
        sa.Column("clay_stabilizer_unit", sa.Text(), nullable=True),
        sa.Column("misc", sa.Text(), nullable=True),
        sa.Column("bulk_modulus", sa.Float(), nullable=True),
        sa.Column("bulk_modulus_unit", sa.Text(), nullable=True),
        sa.Column("base_fluid_density", sa.Float(), nullable=True),
        sa.Column("base_fluid_type", sa.String(length=255), nullable=True),
        sa.Column("max_conc_density", sa.Float(), nullable=True),
        sa.Column("design_acid_vol", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "client",
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("id", sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column("client_uuid", sa.String(length=36), nullable=False),
        sa.Column("client_name", sa.Text(), nullable=True),
        sa.Column("customer_field_rep_id", sa.Text(), nullable=True),
        sa.Column("project_id", sa.BigInteger(), nullable=True),
        sa.Column("operator_name", sa.Text(), nullable=True),
        sa.Column("service_company_name", sa.Text(), nullable=True),
        sa.Column("wireline_company", sa.Text(), nullable=True),
        sa.Column("other_comments", sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "county_name",
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("county_name", sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "crew",
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.Text(), nullable=False),
        sa.Column("shift", sa.Text(), nullable=False),
        sa.Column("role", sa.Enum("admin", "manager", "engineer"), nullable=False),
        sa.Column("manager_id", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "customer_field_rep",
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.Text(), nullable=False),
        sa.Column("email", sa.Text(), nullable=True),
        sa.Column("customer_field_rep_num", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "default_advance_val",
        sa.Column("id", sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column("well_id", sa.Integer(), nullable=True),
        sa.Column("model", sa.String(length=40), nullable=True),
        sa.Column("response", sa.String(length=40), nullable=True),
        sa.Column("source", sa.String(length=40), nullable=True),
        sa.Column("viscosity", sa.Float(), nullable=True),
        sa.Column("density", sa.Float(), nullable=True),
        sa.Column("compressibility", sa.Float(), nullable=True),
        sa.Column("f_low_hz", sa.Float(), nullable=True),
        sa.Column("f_high_hz", sa.Float(), nullable=True),
        sa.Column("new_sample_rate", sa.Float(), nullable=True),
        sa.Column("data_sample_rate", sa.Float(), nullable=True),
        sa.Column("algorithm", sa.String(length=40), nullable=True),
        sa.Column("grid_density", sa.Float(), nullable=True),
        sa.Column("weighting", sa.String(length=10), nullable=True),
        sa.Column("wlevexp", sa.Float(), nullable=True),
        sa.Column("loop", sa.String(length=10), nullable=True),
        sa.Column("method", sa.String(length=20), nullable=True),
        sa.Column("tolerance", sa.Float(), nullable=True),
        sa.Column("interation", sa.Integer(), nullable=True),
        sa.Column("layer", sa.Integer(), nullable=True),
        sa.Column("total_width", sa.Float(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "default_param_val",
        sa.Column("id", sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column("well_id", sa.Integer(), nullable=True),
        sa.Column("c1_min", sa.Float(), nullable=True),
        sa.Column("c2_min", sa.Float(), nullable=True),
        sa.Column("c1_max", sa.Float(), nullable=True),
        sa.Column("c2_max", sa.Float(), nullable=True),
        sa.Column("c3_min", sa.Float(), nullable=True),
        sa.Column("c3_max", sa.Float(), nullable=True),
        sa.Column("q_min", sa.Integer(), nullable=True),
        sa.Column("q_max", sa.Integer(), nullable=True),
        sa.Column("k_min", sa.Float(), nullable=True),
        sa.Column("k_max", sa.Float(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "default_val",
        sa.Column("id", sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column("well_id", sa.Integer(), nullable=False),
        sa.Column("pres", sa.Float(), nullable=True),
        sa.Column("young", sa.Float(), nullable=True),
        sa.Column("overburden", sa.Float(), nullable=True),
        sa.Column("poisson", sa.Float(), nullable=True),
        sa.Column("eta_cp", sa.Integer(), nullable=True),
        sa.Column("fuildt", sa.Integer(), nullable=True),
        sa.Column("tect", sa.Float(), nullable=True),
        sa.Column("fuild_density", sa.Float(), nullable=True),
        sa.Column("diverter_time", sa.Float(), nullable=True),
        sa.Column("met_res", sa.Float(), nullable=True),
        sa.Column("ffkw_correction", sa.Integer(), nullable=True),
        sa.Column("k_mpa", sa.Integer(), nullable=True),
        sa.Column("nu_lim", sa.Integer(), nullable=True),
        sa.Column("per_red", sa.Integer(), nullable=True),
        sa.Column("start1", sa.Integer(), nullable=True),
        sa.Column("beta_ss", sa.Float(), nullable=True),
        sa.Column("st_lim", sa.Integer(), nullable=True),
        sa.Column("biot", sa.Integer(), nullable=True),
        sa.Column("shadow", sa.Integer(), nullable=True),
        sa.Column("fit_end_point", sa.Integer(), nullable=True),
        sa.Column("NG", sa.Integer(), nullable=True),
        sa.Column("breaker_YN", sa.String(length=30), nullable=True),
        sa.Column("passion_method", sa.Integer(), nullable=True),
        sa.Column("plotraw_YN", sa.String(length=30), nullable=True),
        sa.Column("use_wns_YN", sa.String(length=30), nullable=True),
        sa.Column("fit_iteration", sa.Integer(), nullable=True),
        sa.Column("strat2", sa.Integer(), nullable=True),
        sa.Column("stage_ques", sa.Integer(), nullable=True),
        sa.Column("stress_shadow_YN", sa.String(length=30), nullable=True),
        sa.Column("skip_losses_YN", sa.String(length=30), nullable=True),
        sa.Column("use_wncuts_YN", sa.String(length=30), nullable=True),
        sa.Column("poisson_var_YN", sa.String(length=30), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "equipment",
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("trailer_id", sa.Integer(), nullable=True),
        sa.Column("powerpack_id", sa.Integer(), nullable=True),
        sa.Column("source_id", sa.Integer(), nullable=True),
        sa.Column("accumulator_id", sa.Integer(), nullable=True),
        sa.Column("hydrophones_id", sa.Integer(), nullable=True),
        sa.Column("hotspot_id", sa.Integer(), nullable=True),
        sa.Column("computer_id", sa.Integer(), nullable=True),
        sa.Column("transducer_id", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "ff_processing_result",
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("timestamp", sa.DateTime(), nullable=True),
        sa.Column("length", sa.Float(), nullable=True),
        sa.Column("width", sa.Float(), nullable=True),
        sa.Column("height", sa.Float(), nullable=True),
        sa.Column("conductivity", sa.Float(), nullable=True),
        sa.Column("minimum_stress", sa.Float(), nullable=True),
        sa.Column("minimun_stress_gradient", sa.Float(), nullable=True),
        sa.Column("net_pressure", sa.Float(), nullable=True),
        sa.Column("fracture_pressure_gradient", sa.Float(), nullable=True),
        sa.Column("reservoir_pressure", sa.Float(), nullable=True),
        sa.Column("reservoir_pressure_gradient", sa.Float(), nullable=True),
        sa.Column("pressure_match", sa.Float(), nullable=True),
        sa.Column("fracture_efficiency", sa.Float(), nullable=True),
        sa.Column("stress_shadow_pressure", sa.Float(), nullable=True),
        sa.Column("calculated_poisson_ratio", sa.Float(), nullable=True),
        sa.Column("stage_id", sa.Integer(), nullable=True),
        sa.Column("ff_parameter_id", sa.Integer(), nullable=True),
        sa.Column("nwb_region_size", sa.Float(), nullable=True),
        sa.Column("nwb_compressibility", sa.Float(), nullable=True),
        sa.Column("ff_version", sa.Text(), nullable=True),
        sa.Column("unit", sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "field_notes",
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("id", sa.BigInteger(), nullable=False),
        sa.Column("well_id", sa.Integer(), nullable=False),
        sa.Column("comment_timestamp", sa.DateTime(), nullable=True),
        sa.Column("comment_content", sa.Text(), nullable=True),
        sa.Column("comment_by", sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "formation_fuild_injection",
        sa.Column("id", sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column("chem_fluid_id", sa.Integer(), nullable=False),
        sa.Column("bbls", sa.Integer(), nullable=True),
        sa.Column("ppg", sa.Float(), nullable=True),
        sa.Column("description", sa.String(length=50), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "job_info",
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("job_id", sa.Integer(), nullable=True),
        sa.Column("job_name", sa.Text(), nullable=False),
        sa.Column("afe_id", sa.Integer(), nullable=True),
        sa.Column("job_type_id", sa.Integer(), nullable=True),
        sa.Column("job_start_date", sa.DateTime(), nullable=True),
        sa.Column("job_end_date", sa.DateTime(), nullable=True),
        sa.Column("project_id", sa.BigInteger(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "job_type",
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("value", sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "location_info",
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("county_name_id", sa.Integer(), nullable=False),
        sa.Column("basin_name_id", sa.Integer(), nullable=False),
        sa.Column("state_id", sa.Integer(), nullable=False),
        sa.Column("job_info_id", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "nf_processing_result",
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("id", sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column("stage_id", sa.Integer(), nullable=False),
        sa.Column("timestamp", sa.DateTime(), nullable=True),
        sa.Column("user_id", sa.Text(), nullable=True),
        sa.Column("c0", sa.Float(), nullable=True),
        sa.Column("c1", sa.Float(), nullable=True),
        sa.Column("c2", sa.Float(), nullable=True),
        sa.Column("c3", sa.Float(), nullable=True),
        sa.Column("q0", sa.Float(), nullable=True),
        sa.Column("q1", sa.Float(), nullable=True),
        sa.Column("q2", sa.Float(), nullable=True),
        sa.Column("q3", sa.Float(), nullable=True),
        sa.Column("fit_error", sa.Float(), nullable=True),
        sa.Column("nf_param_id", sa.Integer(), nullable=True),
        sa.Column("connect_ops_risk", sa.Float(), nullable=True),
        sa.Column("connect_efficiency", sa.Float(), nullable=True),
        sa.Column("connect_condition", sa.Float(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "pad",
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("pad_uuid", sa.String(length=36), nullable=False),
        sa.Column("project_id", sa.BigInteger(), nullable=False),
        sa.Column("pad_name", sa.Text(), nullable=False),
        sa.Column("number_of_wells", sa.Integer(), nullable=True),
        sa.Column("well_spacing", sa.Float(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "perforation",
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("id", sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column("stage_id", sa.Integer(), nullable=True),
        sa.Column("order_num", sa.Integer(), nullable=True),
        sa.Column("ordinal", sa.Float(), nullable=True),
        sa.Column("top_measured_depth", sa.Float(), nullable=True),
        sa.Column("bottom_measured_depth", sa.Float(), nullable=True),
        sa.Column("depth_unit", sa.Text(), nullable=True),
        sa.Column("shot_number", sa.Integer(), nullable=True),
        sa.Column("shot_density", sa.Float(), nullable=True),
        sa.Column("shot_density_unit", sa.Text(), nullable=True),
        sa.Column("shot_count", sa.Integer(), nullable=True),
        sa.Column("phasing", sa.Text(), nullable=True),
        sa.Column("conveyance_method", sa.Text(), nullable=True),
        sa.Column("charge_type", sa.Text(), nullable=True),
        sa.Column("charge_size", sa.Float(), nullable=True),
        sa.Column("charge_size_unit", sa.Text(), nullable=True),
        sa.Column("estimated_hole_diameter", sa.Float(), nullable=True),
        sa.Column("estimated_hole_diameter_unit", sa.Text(), nullable=True),
        sa.Column("perf_plug_num", sa.Integer(), nullable=True),
        sa.Column("perf_start_time", sa.DateTime(), nullable=True),
        sa.Column("perf_end_time", sa.DateTime(), nullable=True),
        sa.Column("bottom_perf", sa.Float(), nullable=True),
        sa.Column("perf_gun_description", sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "project",
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("id", sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("project_uuid", sa.String(length=36), nullable=False),
        sa.Column("project_name", sa.Text(), nullable=False),
        sa.Column("client_id", sa.Integer(), nullable=False),
        sa.Column("equipment_id", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "project_crew",
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column(
            "project_crew_id", sa.BigInteger(), autoincrement=True, nullable=False
        ),
        sa.Column("project_id", sa.BigInteger(), nullable=False),
        sa.Column("crew_id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("project_crew_id"),
    )
    op.create_table(
        "proppant",
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("id", sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column("stage_id", sa.Integer(), nullable=True),
        sa.Column("proppant_name", sa.String(length=35), nullable=True),
        sa.Column("prop_mass", sa.Float(), nullable=True),
        sa.Column("mass_unit", sa.String(length=10), nullable=True),
        sa.Column("material", sa.String(length=25), nullable=True),
        sa.Column("mesh_size", sa.Float(), nullable=True),
        sa.Column("avg_concentration", sa.Float(), nullable=True),
        sa.Column("avg_concentration_unit", sa.String(length=10), nullable=True),
        sa.Column("max_concentration", sa.Float(), nullable=True),
        sa.Column("max_concentration_unit", sa.String(length=10), nullable=True),
        sa.Column("bulk_density", sa.Integer(), nullable=True),
        sa.Column("specific_gravity", sa.Float(), nullable=True),
        sa.Column("actual_lbs", sa.Float(), nullable=True),
        sa.Column("designed_lbs", sa.Float(), nullable=True),
        sa.Column("total_pumped_lbs", sa.Float(), nullable=True),
        sa.Column("proppant_type_start_time", sa.DateTime(), nullable=True),
        sa.Column("proppant_end_start_time", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "stage",
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("id", sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column("stage_uuid", sa.String(length=36), nullable=False),
        sa.Column("well_id", sa.Integer(), nullable=True),
        sa.Column("stage_number", sa.Integer(), nullable=True),
        sa.Column("number_of_cluster", sa.Integer(), nullable=True),
        sa.Column(
            "stage_start_time", sa.Numeric(precision=25, scale=10), nullable=True
        ),
        sa.Column("stage_end_time", sa.Numeric(precision=25, scale=10), nullable=True),
        sa.Column("plug_depth", sa.Float(), nullable=True),
        sa.Column("calc_net_pressure_result", sa.Float(), nullable=True),
        sa.Column("observed_net_pressure", sa.Float(), nullable=True),
        sa.Column("inline_density", sa.Float(), nullable=True),
        sa.Column("blender_density", sa.Float(), nullable=True),
        sa.Column("calc_bh_density", sa.Float(), nullable=True),
        sa.Column("bottomhole_bhp", sa.Float(), nullable=True),
        sa.Column("bottomhole_bht", sa.Float(), nullable=True),
        sa.Column("frac_model_bhp", sa.Float(), nullable=True),
        sa.Column("total_pumpdown_volume", sa.Float(), nullable=True),
        sa.Column("poisson_ratio", sa.Float(), nullable=True),
        sa.Column("pr_gradient", sa.Float(), nullable=True),
        sa.Column("overburden_num", sa.Float(), nullable=True),
        sa.Column("pumping_fluid_viscosity", sa.Float(), nullable=True),
        sa.Column("pumping_fluid_density", sa.Float(), nullable=True),
        sa.Column("pumping_fluid_type", sa.Text(), nullable=True),
        sa.Column("tectonic_gradient", sa.Float(), nullable=True),
        sa.Column("pore_pressure", sa.Float(), nullable=True),
        sa.Column("sleeve_name", sa.Text(), nullable=True),
        sa.Column("sleeve_ordinal", sa.Integer(), nullable=True),
        sa.Column("sleeve_top_measured_depth", sa.Float(), nullable=True),
        sa.Column("sleeve_bottom_measured_depth", sa.Float(), nullable=True),
        sa.Column("sleeve_depth_unit", sa.Text(), nullable=True),
        sa.Column("sleeve_port_size", sa.Float(), nullable=True),
        sa.Column("sleeve_port_size_unit", sa.Text(), nullable=True),
        sa.Column("sleeve_ball_size", sa.Float(), nullable=True),
        sa.Column("sleeve_ball_size_unit", sa.Text(), nullable=True),
        sa.Column("sleeve_seat_id", sa.Text(), nullable=True),
        sa.Column("sleeve_manufacturer", sa.Text(), nullable=True),
        sa.Column("sleeve_model", sa.Text(), nullable=True),
        sa.Column("sleeve_toe_shift_pressure", sa.Integer(), nullable=True),
        sa.Column("sleeve_toe_burst_pressure", sa.Integer(), nullable=True),
        sa.Column("additional", mysql.JSON(), nullable=True),
        sa.Column("is_approved", mysql.TINYINT(), nullable=True),
        sa.Column("diverter_type", sa.String(length=255), nullable=True),
        sa.Column("pumped_diverter", sa.String(length=255), nullable=True),
        sa.Column("spf", sa.String(length=255), nullable=True),
        sa.Column("stage_event", sa.String(length=255), nullable=True),
        sa.Column("designed_acid_vol", sa.Float(), nullable=True),
        sa.Column("designed_flush_vol", sa.Float(), nullable=True),
        sa.Column("designed_max_prop", sa.Float(), nullable=True),
        sa.Column("designed_slurry_vol", sa.Float(), nullable=True),
        sa.Column("designed_total_clean_fluid_vol", sa.Float(), nullable=True),
        sa.Column("designed_proppant", sa.Float(), nullable=True),
        sa.Column("designed_pad_vol", sa.Float(), nullable=True),
        sa.Column("frac_design", sa.String(length=255), nullable=True),
        sa.Column("plug_seat_technique", sa.String(length=255), nullable=True),
        sa.Column("plug_type", sa.String(length=255), nullable=True),
        sa.Column("plug_name", sa.String(length=50), nullable=True),
        sa.Column("data_collection", sa.String(length=255), nullable=True),
        sa.Column("is_acid", sa.String(length=55), nullable=True),
        sa.Column("top_perf_Displacement_volume", sa.Float(), nullable=True),
        sa.Column("bottom_perf_Displacement_volume", sa.Float(), nullable=True),
        sa.Column("plug_displacement_volume", sa.Float(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "stage_avg",
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("id", sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column("stage_id", sa.Integer(), nullable=False),
        sa.Column("breakdown_pressure", sa.Float(), nullable=True),
        sa.Column("isip", sa.Float(), nullable=True),
        sa.Column("frac_gradient", sa.Float(), nullable=True),
        sa.Column("diverter", sa.Float(), nullable=True),
        sa.Column("acid", sa.Float(), nullable=True),
        sa.Column("open_well_pressure", sa.Float(), nullable=True),
        sa.Column("isip_5min", sa.Float(), nullable=True),
        sa.Column("isip_10min", sa.Float(), nullable=True),
        sa.Column("isip_15min", sa.Float(), nullable=True),
        sa.Column("time_to_max_rate", sa.Float(), nullable=True),
        sa.Column("avg_pressure", sa.Float(), nullable=True),
        sa.Column("max_pressure", sa.Float(), nullable=True),
        sa.Column("slickwater_volume", sa.Float(), nullable=True),
        sa.Column("total_slurry", sa.Float(), nullable=True),
        sa.Column("total_clean", sa.Float(), nullable=True),
        sa.Column("total_proppant_lbs", sa.Float(), nullable=True),
        sa.Column("avg_rate", sa.Float(), nullable=True),
        sa.Column("max_rate", sa.Float(), nullable=True),
        sa.Column("100_mesh", sa.Float(), nullable=True),
        sa.Column("30_50_mesh", sa.Float(), nullable=True),
        sa.Column("40_70_mesh", sa.Float(), nullable=True),
        sa.Column("20_40_mesh", sa.Float(), nullable=True),
        sa.Column("micro_prop", sa.Float(), nullable=True),
        sa.Column("friction_reducer", sa.Float(), nullable=True),
        sa.Column("gel", sa.Float(), nullable=True),
        sa.Column("crosslink", sa.Float(), nullable=True),
        sa.Column("additional", mysql.JSON(), nullable=True),
        sa.Column("flush_volume", sa.Float(), nullable=True),
        sa.Column("max_prop_conc", sa.Float(), nullable=True),
        sa.Column("pad_vol", sa.Integer(), nullable=True),
        sa.Column("opening_well", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "state",
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("value", sa.Text(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(length=50), nullable=False),
        sa.Column("email", sa.String(length=150), nullable=False),
        sa.Column("password", sa.String(length=255), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("user_uuid", sa.String(length=36), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "project_user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("project_id", sa.BigInteger(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "well",
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("well_uuid", sa.String(length=36), nullable=False),
        sa.Column("pad_id", sa.Integer(), nullable=False),
        sa.Column("well_name", sa.Text(), nullable=True),
        sa.Column("well_api", sa.Text(), nullable=True),
        sa.Column("formation", sa.String(length=255), nullable=True),
        sa.Column("num_stages", sa.Integer(), nullable=True),
        sa.Column("total_planned_stage", sa.Integer(), nullable=True),
        sa.Column("total_perfs", sa.Integer(), nullable=True),
        sa.Column("total_clusters", sa.Integer(), nullable=True),
        sa.Column("frac_system", sa.Text(), nullable=True),
        sa.Column("fluid_system", sa.Text(), nullable=True),
        sa.Column("well_start_time", sa.DateTime(), nullable=True),
        sa.Column("well_end_time", sa.DateTime(), nullable=True),
        sa.Column("bottom_hole_latitude", sa.Float(), nullable=True),
        sa.Column("bottom_hole_longitude", sa.Float(), nullable=True),
        sa.Column("surface_longitude", sa.Float(), nullable=True),
        sa.Column("surface_latitude", sa.Float(), nullable=True),
        sa.Column("lateral_length", sa.Float(), nullable=True),
        sa.Column("lateral_length_unit", sa.Text(), nullable=True),
        sa.Column("measured_depth", sa.Float(), nullable=True),
        sa.Column("vertical_depth", sa.Float(), nullable=True),
        sa.Column("vertical_depth_unit", sa.Text(), nullable=True),
        sa.Column("estimated_surface_vol", sa.Float(), nullable=True),
        sa.Column("estimated_bbls", sa.Float(), nullable=True),
        sa.Column("estimated_gallons", sa.Float(), nullable=True),
        sa.Column("casing_od", sa.Float(), nullable=True),
        sa.Column("casing_wt", sa.Float(), nullable=True),
        sa.Column("casing_id", sa.Float(), nullable=True),
        sa.Column("casing_depth_md", sa.Float(), nullable=True),
        sa.Column("casing_tol", sa.Float(), nullable=True),
        sa.Column("liner1_od", sa.Float(), nullable=True),
        sa.Column("liner1_wt", sa.Float(), nullable=True),
        sa.Column("liner1_id", sa.Text(), nullable=True),
        sa.Column("liner1_depth_md", sa.Float(), nullable=True),
        sa.Column("liner1_tol", sa.Float(), nullable=True),
        sa.Column("liner2_od", sa.Float(), nullable=True),
        sa.Column("liner2_wt", sa.Float(), nullable=True),
        sa.Column("liner2_id", sa.Text(), nullable=True),
        sa.Column("liner2_depth_md", sa.Float(), nullable=True),
        sa.Column("liner2_tol", sa.Float(), nullable=True),
        sa.Column("measured_depth_unit", sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("well")
    op.drop_table("project_user")
    op.drop_table("user")
    op.drop_table("state")
    op.drop_table("stage_avg")
    op.drop_table("stage")
    op.drop_table("proppant")
    op.drop_table("project_crew")
    op.drop_table("project")
    op.drop_table("perforation")
    op.drop_table("pad")
    op.drop_table("nf_processing_result")
    op.drop_table("location_info")
    op.drop_table("job_type")
    op.drop_table("job_info")
    op.drop_table("formation_fuild_injection")
    op.drop_table("field_notes")
    op.drop_table("ff_processing_result")
    op.drop_table("equipment")
    op.drop_table("default_val")
    op.drop_table("default_param_val")
    op.drop_table("default_advance_val")
    op.drop_table("customer_field_rep")
    op.drop_table("crew")
    op.drop_table("county_name")
    op.drop_table("client")
    op.drop_table("chem_fluids")
    op.drop_table("basin_name")
    op.drop_table("active_data")
    # ### end Alembic commands ###
